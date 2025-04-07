head = """
<!DOCTYPE html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata:wght@300&family=Oswald&display=swap"
rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@1,300&display=swap"
rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Inconsolata&display=swap" rel="stylesheet">
\n
<!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous">
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous"></script>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>


%s
</head>

<body>
<nav class="navbar sticky-top navbar-light bg-light">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="https://raw.githubusercontent.com/abhaykatheria/json2tree/main/J2T.png" width="80" height="30" class="d-inline-block align-top" alt=""> JSON2tree
        </a>
        <div class="d-flex">
            <div class="input-group">
                <input type="text" id="searchInput" class="form-control" placeholder="Search...">
                <button class="btn btn+-outline-secondary" type="button" id="searchPrev">
                    <span>↑</span>
                </button>
                <button class="btn btn-outline-secondary" type="button" id="searchNext">
                    <span>↓</span>
                </button>
                <span class="input-group-text" id="searchCount">0/0</span>
                <div class="input-group-text">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="caseSensitive">
                        <label class="form-check-label" for="caseSensitive">Case sensitive</label>
                    </div>
                </div>
            </div>
        </div>
    </div>
</nav>
"""