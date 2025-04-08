css = '''
<style>
/* General styling improvements */
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', sans-serif;
    line-height: 1.5;
    color: #2d3748;
    background-color: #f8fafc;
    padding: 20px;
}

/* Tree structure styling */
ul, #myUL {
    list-style-type: none;
}

li {
    padding-top: 6px;
    padding-bottom: 6px;
    transition: background-color 0.2s;
}

li:hover {
    background-color: #f1f5f9;
    border-radius: 4px;
}

#myUL {
    margin: 0;
    padding: 0;
}

/* Caret styling for tree expansion */
.caret {
    cursor: pointer;
    user-select: none;
    font-family: 'JetBrains Mono', 'Fira Code', 'Inconsolata', monospace;
    font-weight: 500;
    color: #334155;
}

.caret::before {
    content: " \\25B6";
    display: inline-block;
    margin-right: 8px;
    color: #64748b;
    transition: transform 0.2s ease;
}

.caret-down::before {
    transform: rotate(90deg);
}

/* Nested elements */
.nested {
    display: none;
    padding-left: 18px;
    border-left: 1px dotted #cbd5e1;
    margin-left: 8px;
}

.active {
    display: block;
}

.header {
    text-align: left;
    background: #f1f5f9;
    padding: 12px;
    border-radius: 6px;
    margin-bottom: 16px;
    border-bottom: 2px solid #e2e8f0;
}

/* Text styling for different elements */
.text-c {
    color: #059669;
    font-family: 'JetBrains Mono', 'Fira Code', 'Inconsolata', monospace;
    font-size: 14px;
}

.text-h {
    font-family: 'JetBrains Mono', 'Fira Code', 'Inconsolata', monospace;
    font-size: 14px;
    color: #1e40af;
    font-weight: 500;
}

/* Search highlighting styles */
.highlighted {
    background-color: #fef9c3;
    padding: 0 2px;
    border-radius: 2px;
    box-shadow: 0 0 1px #eab308;
}

/* Current highlight style */
.current-highlight {
    background-color: #fef9c3;
    color: inherit;
    padding: 0 2px;
    border-radius: 2px;
    box-shadow: 0 0 0 2px #f59e0b;
    position: relative;
    z-index: 1;
}

/* Add some styling for JSON values by type */
.json-string { color: #16a34a; }
.json-number { color: #2563eb; }
.json-boolean { color: #9333ea; }
.json-null { color: #94a3b8; font-style: italic; }
</style>\n
'''
