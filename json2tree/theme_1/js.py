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
    
    // Hide None values functionality
    $("#hideNoneValues").on("change", function() {
        if($(this).prop("checked")) {
            $(".none-value").addClass("hidden");
        } else {
            $(".none-value").removeClass("hidden");
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
});
</script>\n
'''