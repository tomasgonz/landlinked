css_general = """
<style>
    .reportview-container .main .block-container {
        padding: 2rem;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
    h1 {
        font-size: 2.5rem;
        font-weight: bold;
    }
    .card {
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem;
        background: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .metric {
        font-size: 1.5rem;
        font-weight: bold;
    }
    /* Floating menu */
    .floating-menu {
        position: fixed;
        top: 50%;
        right: 20px;
        transform: translateY(-50%);
        background: #ffffff;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        transition: right 0.3s ease;
    }
    .floating-menu:hover {
        right: 0;
    }
    .floating-menu a {
        text-decoration: none;
        color: #000000;
        font-weight: 600;
        display: block;
        padding: 5px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    .floating-menu a:hover {
        color: #ffffff;
        background-color: #007BFF;
        border-radius: 5px;
    }
    .floating-menu .menu-header {
        cursor: pointer;
        font-weight: bold;
    }
    .menu-content {
        display: none;
    }
    .menu-content a {
        display: block;
        padding: 5px;
        margin: 5px 0;
    }
    .menu-header:hover + .menu-content, .menu-content:hover {
        display: block;
    }
    </style>
    """

css_menu = """
    <div class="floating-menu">
        <div class="menu-header">Sections</div>
        <div class="menu-content">
            <a href="#environment">Environment</a>
            <a href="#labor-force">Labor Force</a>
            <a href="#population">Population</a>
            <a href="#education">Education</a>
            <a href="#connectivity">Connectivity</a>
            <a href="#economy">Economy</a>
        </div>
    i</div>
    """
