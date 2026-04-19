@app.route("/user21", methods=["GET", "POST"])
def user21():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        return render_template(
            "result21.html",
            email=email,
            password=password
        )

    return render_template("index21.html")
