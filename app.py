from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    # Designs, grouped by who it's for
    designs = [
        {
            "id": "riverview_block",
            "label": "Riverview Block Spirit",
            "tag": "Riverview",
            "description": "Bold Riverview Falcons block text, great for spirit wear drops.",
            "groups": ["Riverview Elementary", "Riverview PTA"]
        },
        {
            "id": "riverview_script",
            "label": "Riverview Script",
            "tag": "Riverview",
            "description": "Soft script style with mascot accent, perfect for moms and staff.",
            "groups": ["Riverview Elementary", "Riverview PTA"]
        },
        {
            "id": "mv_game_day",
            "label": "MV Game Day",
            "tag": "MV Cheer",
            "description": "High-energy Mill Valley game day lettering for cheerleaders & fans.",
            "groups": ["MV Cheerleading"]
        },
        {
            "id": "mv_stack",
            "label": "MV Stacked Logo",
            "tag": "MV Cheer",
            "description": "Clean stacked MV + paw/mascot mark for hoodies and crews.",
            "groups": ["MV Cheerleading"]
        },
        {
            "id": "desoto_cheer_classic",
            "label": "De Soto Cheer Classic",
            "tag": "De Soto",
            "description": "Classic cheer arched lettering with De Soto colors in mind.",
            "groups": ["De Soto Cheerleading"]
        },
        {
            "id": "desoto_side_mark",
            "label": "De Soto Sleeve Mark",
            "tag": "De Soto",
            "description": "Simple chest logo with cheer detail down the sleeve.",
            "groups": ["De Soto Cheerleading"]
        },
        {
            "id": "small_biz_logo",
            "label": "Small Business Logo Front",
            "tag": "Business",
            "description": "Clean left-chest logo placement, ideal for staff apparel.",
            "groups": ["Small business team"]
        },
        {
            "id": "small_biz_front_back",
            "label": "Brand Front + Back",
            "tag": "Business",
            "description": "Logo on the front, tagline or website across the back.",
            "groups": ["Small business team"]
        },
        {
            "id": "family_trip",
            "label": "Family Trip / Event",
            "tag": "Family",
            "description": "Matching shirts or hoodies for a family trip, reunion, or event.",
            "groups": ["Family / Friends group"]
        },
        {
            "id": "custom_idea",
            "label": "Custom Idea From Scratch",
            "tag": "Custom",
            "description": "I have an idea and need help bringing it to life.",
            "groups": [
                "Riverview Elementary",
                "Riverview PTA",
                "MV Cheerleading",
                "De Soto Cheerleading",
                "Small business team",
                "Family / Friends group",
                "other"
            ]
        },
    ]

    selected_design_id = None
    selected_design = None

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        group = request.form.get("group")
        group_other = request.form.get("group_other")
        item_type = request.form.get("item_type")
        selected_design_id = request.form.get("design_id")

        # Final group name
        if group == "other" and group_other:
            final_group = group_other
        else:
            final_group = group or group_other

        # Look up design
        for d in designs:
            if d["id"] == selected_design_id:
                selected_design = d
                break

        print("----- New mock order -----")
        print("Name:", name)
        print("Email:", email)
        print("Group:", final_group)
        print("Item type:", item_type)
        print("Selected design ID:", selected_design_id)
        print(
            "Selected design label:",
            selected_design["label"] if selected_design else None,
        )
        print("--------------------------")

        return render_template(
            "order.html",
            submitted=True,
            name=name,
            designs=designs,
            selected_design_id=selected_design_id,
            selected_design=selected_design,
        )

    # GET (first load)
    return render_template(
        "order.html",
        submitted=False,
        name=None,
        designs=designs,
        selected_design_id=None,
        selected_design=None,
    )

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
