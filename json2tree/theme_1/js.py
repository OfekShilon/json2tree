js = '''
<script>
var toggler = document.getElementsByClassName("caret");
var i;
for (i = 0; i < toggler.length; i++) {
    toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
}
)}

// Search functionality
$(document).ready(function() {
    var searchResults = [];
    var currentResultIndex = -1;
    
    // Hide None values on page load since the checkbox is checked by default
    $(".none-value").addClass("hidden");
    
    // Hide None values functionality
    $("#hideNoneValues").on("change", function() {
        if($(this).prop("checked")) {
            $(".none-value").addClass("hidden");
        } else {
            $(".none-value").removeClass("hidden");
        }
    });
    
    // Collapse single children functionality
    $("#collapseSingleChildren").on("change", function() {
        if($(this).prop("checked")) {
            $("body").addClass("collapse-singles");
            
            // If some nodes are expanded, make sure the path is visible
            $(".caret-down").each(function() {
                var $parent = $(this).parent();
                if ($parent.hasClass("single-child-parent")) {
                    // Keep the node and its children visible
                    $parent.find("> .single-child-container").show();
                    $parent.find("> .single-child-container > .nested").addClass("active");
                    $parent.find("> .collapsed-path").hide();
                }
            });
        } else {
            $("body").removeClass("collapse-singles");
        }
    });
    
    // Add special handling for caret clicks on single child parents
    $(document).on("click", ".single-child-parent > .caret", function() {
        var $parent = $(this).parent();
        var isCollapsingSingleChildren = $("#collapseSingleChildren").prop("checked");
        
        if (isCollapsingSingleChildren) {
            if ($(this).hasClass("caret-down")) {
                // Node is being expanded
                $parent.find("> .single-child-container").show();
                $parent.find("> .collapsed-path").hide();
            } else {
                // Node is being collapsed
                $parent.find("> .single-child-container").hide();
                $parent.find("> .collapsed-path").show();
            }
        }
    });
    
    function performSearch(searchTerm) {
        if (!searchTerm) {
            // Clear all highlights if search is empty
            $(".highlighted").removeClass("highlighted");
            $("#searchCount").text("0/0");
            searchResults = [];
            currentResultIndex = -1;
            return;
        }
        
        // Clear previous highlights
        $(".highlighted").removeClass("highlighted");
        
        // Find all elements containing the search term
        searchResults = [];
        
        // Get case sensitivity setting
        var isCaseSensitive = $("#caseSensitive").prop("checked");
        
        // Search in all text content within tree elements
        $("li span").each(function() {
            var $this = $(this);
            var text = $this.text();
            
            // Skip if this is just a structural element
            if (!text.trim()) return;
            
            // Check if the element contains the search term (respecting case sensitivity)
            var containsSearchTerm = false;
            if (isCaseSensitive) {
                containsSearchTerm = text.indexOf(searchTerm) >= 0;
            } else {
                containsSearchTerm = text.toLowerCase().indexOf(searchTerm.toLowerCase()) >= 0;
            }
            
            if (containsSearchTerm) {
                // Highlight the found term using simple string operations
                var highlightedText = highlightPlainText(text, searchTerm, isCaseSensitive);
                $this.html(highlightedText);
                
                // Store the result
                searchResults.push($this);
            }
        });
        
        // Expand all parent nodes of search results
        if (searchResults.length > 0) {
            // First expand all parent nodes for all search results
            for (var i = 0; i < searchResults.length; i++) {
                expandParents(searchResults[i]);
            }
            
            // Now scroll to the first result
            scrollToResult(0);
        }
        
        // Update count
        $("#searchCount").text(searchResults.length > 0 ? 
            "1/" + searchResults.length : "0/0");
            
        // Reset current index
        currentResultIndex = searchResults.length > 0 ? 0 : -1;
    }
    
    // Function to highlight text without using regex
    function highlightPlainText(text, searchTerm, isCaseSensitive) {
        var result = '';
        var remainingText = text;
        var searchTermLower = searchTerm.toLowerCase();
        
        while (remainingText.length > 0) {
            var index = -1;
            if (isCaseSensitive) {
                index = remainingText.indexOf(searchTerm);
            } else {
                index = remainingText.toLowerCase().indexOf(searchTermLower);
            }
            
            if (index >= 0) {
                // Add text before the match
                result += remainingText.substring(0, index);
                
                // Add the highlighted match (preserving original case)
                var matchedText = remainingText.substring(index, index + searchTerm.length);
                result += '<span class="highlighted">' + matchedText + '</span>';
                
                // Continue with the remaining text
                remainingText = remainingText.substring(index + searchTerm.length);
            } else {
                // No more matches, add the rest of the text
                result += remainingText;
                break;
            }
        }
        
        return result;
    }
    
    function expandParents($element) {
        var $parent = $element.closest('li');
        while ($parent.length > 0) {
            // Expand this level
            var $caret = $parent.find('> span.caret');
            var $nested = $parent.find('> ul.nested');
            if ($caret.length && $nested.length && !$nested.hasClass('active')) {
                $caret.addClass('caret-down');
                $nested.addClass('active');
                
                // Handle single children collapse logic
                if ($parent.hasClass("single-child-parent") && $("#collapseSingleChildren").prop("checked")) {
                    $parent.find("> .single-child-container").show();
                    $parent.find("> .collapsed-path").hide();
                }
            }
            $parent = $parent.parent().closest('li');
        }
    }
    
    function scrollToResult(index) {
        if (index < 0 || index >= searchResults.length) return;
        
        // Remove 'current' class from all results
        $(".current-highlight").removeClass("current-highlight");
        
        // Add 'current' class to current result
        var $current = searchResults[index];
        $current.find(".highlighted").addClass("current-highlight");
        
        // Update counter
        $("#searchCount").text((index + 1) + "/" + searchResults.length);
        
        // Scroll to view
        $current[0].scrollIntoView({
            behavior: 'smooth',
            block: 'center'
        });
    }
    
    // Enter key handler for search input
    $("#searchInput").on("keyup", function(e) {
        if (e.key === "Enter") {
            var searchTerm = $(this).val();
            performSearch(searchTerm);
        }
    });
    
    // Case-sensitive checkbox change handler
    $("#caseSensitive").on("change", function() {
        var searchTerm = $("#searchInput").val();
        if (searchTerm) {
            performSearch(searchTerm);
        }
    });
    
    // Next button handler
    $("#searchNext").on("click", function() {
        if (searchResults.length === 0) return;
        
        currentResultIndex++;
        if (currentResultIndex >= searchResults.length) {
            currentResultIndex = 0;
        }
        
        scrollToResult(currentResultIndex);
    });
    
    // Previous button handler
    $("#searchPrev").on("click", function() {
        if (searchResults.length === 0) return;
        
        currentResultIndex--;
        if (currentResultIndex < 0) {
            currentResultIndex = searchResults.length - 1;
        }
        
        scrollToResult(currentResultIndex);
    });
    
    // Mark single child nodes after DOM is fully loaded
    setTimeout(function() {
        markSingleChildren();
    }, 100);
    
    function markSingleChildren() {
        // Find all ul.nested elements that have exactly one child li
        $("ul.nested").each(function() {
            var $ul = $(this);
            var $childLis = $ul.children("li");
            
            // If there's exactly one child
            if ($childLis.length === 1) {
                var $parentLi = $ul.parent("li");
                if ($parentLi.length) {
                    var $parentCaret = $parentLi.children(".caret");
                    var $childCaret = $childLis.children(".caret");
                    
                    if ($parentCaret.length && $childCaret.length) {
                        // Get the child's text
                        var childText = $childLis.children(".caret").text().trim();
                        
                        // Add classes for styling
                        $parentLi.addClass("single-child-parent");
                        $ul.addClass("single-child-container");
                        
                        // Add collapsed path element
                        var $collapsedPath = $('<span class="collapsed-path">' + childText + '</span>');
                        $parentCaret.after($collapsedPath);
                        
                        // If there are more levels, add an indicator
                        if ($childLis.find(".nested").length) {
                            $collapsedPath.after('<span class="collapsed-descendants">...</span>');
                        }
                    }
                }
            }
        });
    }
});
</script>\n
'''