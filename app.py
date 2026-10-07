from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>HANSON TECH</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #050505;
            color: white;
        }

        header {
            padding: 22px;
            text-align: center;
            border-bottom: 1px solid #333;
        }

        header h2 {
            color: #00c8ff;
            font-size: 28px;
        }

        header p {
            margin-top: 8px;
        }
nav {
    margin-top: 18px;
}

nav a {
    color: white;
    text-decoration: none;
    margin: 0 12px;
    font-weight: bold;
}

nav a:hover {
    color: #00c8ff;
}

        .hero {
            text-align: center;
            padding: 80px 20px;
        }

        .hero h1 {
            font-size: 55px;
            margin-bottom: 20px;
        }

        .hero p {
            color: #ccc;
            font-size: 19px;
        }

        .button {
            display: inline-block;
            margin-top: 25px;
            padding: 14px 25px;
            background: #00c8ff;
            color: #000;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
        }

        section {
            padding: 60px 8%;
            text-align: center;
        }

        section h2 {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .subtitle {
            color: #aaa;
            margin-bottom: 35px;
        }

        .search-box {
            width: 100%;
            max-width: 500px;
            padding: 15px 20px;
            margin: 0 auto 35px auto;
            display: block;
            background: #111;
            color: white;
            border: 1px solid #333;
            border-radius: 10px;
            font-size: 16px;
            outline: none;
        }

        .search-box:focus {
            border-color: #00c8ff;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

       .product {
    transition: 0.3s ease;
}

.product:hover {
    transform: translateY(-8px);
    border-color: #00c8ff;
    box-shadow: 0 10px 30px rgba(0, 200, 255, 0.2);
}

        .icon {
            margin-bottom: 15px;
        }

       .icon img {
    width: 100%;
    height: 200px;
    object-fit: contain;
    display: block;
    transition: 0.3s ease;
}

.product:hover .icon img {
    transform: scale(1.05);
}

        .product h3 {
            margin-bottom: 10px;
        }

        .product p {
            color: #bbb;
            line-height: 1.5;
        }

        .order {
            background: #0b1820;
        }
.contact {
    background: #080f14;
    text-align: center;
}

.contact p {
    margin-bottom: 10px;
    color: #ccc;
}

        footer {
            text-align: center;
            padding: 30px;
            color: #888;
            border-top: 1px solid #222;
        }

        @media (max-width: 600px) {
            .hero h1 {
                font-size: 40px;
            }

            section h2 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

<header>
    <img src="/static/images/logo/logo.jpeg" alt="HANSON TECH Logo" class="logo">

    <p>iSell • iBuy • iSwap</p>
    <nav>
        <a href="#home">Home</a>
        <a href="#products">Products</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<div class="hero" id="home">
    <p>
        Smartphones • Gadgets • Accessories • Digital Services
    </p>

    <a class="button" href="#products">
        Shop Now
    </a>
</div>


<section id="products">

    <h2>Our Products</h2>

    <p class="subtitle">
        Quality gadgets and accessories available from HANSON TECH.
    </p>

    <input
        type="text"
        id="searchInput"
        class="search-box"
        placeholder="Search for a product..."
    >


    <div class="products" id="productList">


        <div class="product">
            <div class="icon">
                <img src="/static/images/images/images.jpg.jfif" alt="iPhones">
            </div>

            <h3>iPhones</h3>

            <p>
                Different iPhone models and storage options available.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20an%20iPhone.">
                Ask About iPhone
            </a>
        </div>


        <div class="product">
            <div class="icon">
                <img src="/static/images/samsungs/images%20(3).jfif" alt="Samsung Phones">
            </div>

            <h3>Samsung Phones</h3>

            <p>
                Samsung smartphones and selected Galaxy devices.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20a%20Samsung%20phone.">
                Ask About Samsung
            </a>
        </div>


        <div class="product">
            <div class="icon">
                <img src="/static/images/airpod/airpods2.jfif" alt="AirPods">
            </div>

            <h3>AirPods & Earbuds</h3>

            <p>
                AirPods, TWS and other wireless audio accessories.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20AirPods%20or%20earbuds.">
                Ask About AirPods
            </a>
        </div>


        <div class="product">
            <div class="icon">
                <img src="/static/images/pb/pb.jfif" alt="Power Banks">
            </div>

            <h3>Power Banks</h3>

            <p>
                Reliable power banks for your everyday charging needs.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20a%20power%20bank.">
                Ask About Power Bank
            </a>
        </div>


        <div class="product">
            <div class="icon">
                <img src="/static/images/wtc/wtc2.jfif" alt="Smart Watches">
            </div>

            <h3>Smart Watches</h3>

            <p>
                Smart watches and wearable accessories.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20a%20smart%20watch.">
                Ask About Smart Watch
            </a>
        </div>


        <div class="product">
            <div class="icon">
                <img src="/static/images/chg/chg.jfif" alt="Chargers & Cables">
            </div>

            <h3>Chargers & Cables</h3>

            <p>
                Fast-charging cables, chargers and phone accessories.
            </p>

            <a class="button"
               href="https://wa.me/2349071875737?text=Hello%20HANSON%20TECH,%20I%20am%20interested%20in%20chargers%20or%20cables.">
                Ask About Chargers
            </a>
        </div>


    </div>

</section>


<section class="contact" id="contact">
    <h2>Contact Us</h2>

    <p class="subtitle">
        Have a question? We'd love to hear from you.
    </p>

    <p>📱 WhatsApp: +234 907 187 5737</p>

    <a class="button" href="https://wa.me/2349071875737">
        Chat With Us
    </a>

</section>
<div style="text-align: center; margin: 30px 0;">
    <a class="button" href="#home">
        Back to Top
    </a>
</div>
<footer>
    © 2026 HANSON TECH
    <br><br>
    iSell • iBuy • iSwap
</footer>


<script>
    const searchInput = document.getElementById("searchInput");
    const products = document.querySelectorAll(".product");

    searchInput.addEventListener("input", function() {
        const searchText = this.value.toLowerCase();

        products.forEach(function(product) {
            const productName = product.querySelector("h3").textContent.toLowerCase();

            if (productName.includes(searchText)) {
                product.style.display = "";
            } else {
                product.style.display = "none";
            }
        });
    });
</script>


</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)