head = """
<!DOCTYPE html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Modern Font Imports -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

<!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
<!-- jQuery -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>


%s
</head>

<body>
<nav class="navbar sticky-top navbar-light bg-light shadow-sm">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="https://raw.githubusercontent.com/abhaykatheria/json2tree/main/J2T.png" width="80" height="30" class="d-inline-block align-top" alt=""> 
            <span style="font-family: 'Inter', sans-serif; font-weight: 600; color: #334155;">JSON2tree</span>
        </a>
        <div class="d-flex">
            <div class="input-group">
                <input type="text" id="searchInput" class="form-control shadow-sm" placeholder="Search..." style="font-family: 'Inter', sans-serif;">
                <button class="btn btn-outline-secondary" type="button" id="searchPrev">
                    <span>↑</span>
                </button>
                <button class="btn btn-outline-secondary" type="button" id="searchNext">
                    <span>↓</span>
                </button>
                <span class="input-group-text" id="searchCount">0/0</span>
                <div class="input-group-text">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="caseSensitive" checked>
                        <label class="form-check-label" for="caseSensitive">Case sensitive search</label>
                    </div>
                </div>
                <div class="input-group-text">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="hideNoneValues" checked>
                        <label class="form-check-label" for="hideNoneValues">Hide None values</label>
                    </div>
                </div>
                <div class="input-group-text">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="collapseSingleChildren">
                        <label class="form-check-label" for="collapseSingleChildren">Collapse single children</label>
                    </div>
                </div>
            </div>
        </div>
    </div>
</nav>
"""