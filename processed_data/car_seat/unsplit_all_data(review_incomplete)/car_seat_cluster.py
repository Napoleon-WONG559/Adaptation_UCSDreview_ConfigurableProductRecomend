clusters = {
    # Example:
    # "Seat Type": {
    #     "rear_facing_only": ["Rear Facing", "Rear forward facing"],
    #     "forward_facing_only": ["Forward Facing", "Front-Facing"],
    #     ...
    # },
    #
    # "Weight Range": {
    #     "infant": [...],
    #     "toddler": [...],
    #     ...
    # }
    "Seat Type" : {
    #"rear_facing_only": [
    "0": [
        "Rear Facing",
        "Rear forward facing",
        "rear forward facing"
    ],

    #"forward_facing_only": [
    "1": [
        "Forward Facing",
        "Front-Facing",
        "Back"
    ],

    #"rear_and_forward_dual_mode": [
    "2": [
        "Rear Facing, Forward Facing",
        "Forward Facing, Rear Facing",
        "Rear & Forward Facing",
        "Rear forward facing, Forward Facing",
        "Rear Facing Forward Facing",
        "Forward / Rear Facing",
        "Forward Facing (GOM, Rear Facing"
    ],

    #"convertible": [
    "3": [
        "Convertible",
        "Convertible Seat",
        "Convertible Seat, Rear Facing"
    ],

    #"ambiguous": [
    "4": [
        "Right Handle",
        "csv_na"
    ]
    },

    #--------------------------------------------------------
    "Weight Range" : {

    # Cluster 1 — "Up To" Infant-Only Ranges
    "0": [
        "Up to 20 Grams lbs",
        "Up to 22 Pounds lbs",
        "Up to 30 Pounds lbs",
        "Up to 32 Pounds lbs",
        "Up to 35 Pounds lbs",
        "Up to 40 Pounds lbs",
        "Up to 40 Pounds, 5 Pounds lbs",
        "Up to 50 Pounds lbs",
        "Up to 70 Pounds lbs",
        "Up to 100 Pounds lbs",
        "Up to 110 Pounds lbs",
        "Up to 120 Pounds lbs",
        "Up to 0.09 Pounds lbs"
    ],

    # Cluster 2 — Very Small Infant Ranges
    "1": [
        "4 Pounds-20 Pounds lbs",
        "4 Pounds-22 Pounds lbs",
        "4 Pounds-11 Pounds lbs",
        "22 Pounds-22 Pounds lbs",
        "5 Pounds-5 Pounds lbs",
        "4 Pounds-4 Pounds lbs",
        "4.5 Pounds-35 Pounds lbs",
        "4.5 Pounds-30 Pounds lbs",
        "3 Pounds-35 Pounds lbs",
        "3 Pounds-40 Pounds lbs",
        "5.5 Pounds-30 Pounds lbs"
    ],

    # Cluster 3 — Infant–Toddler Ranges
    "2": [
        "4 Pounds-30 Pounds lbs",
        "4 Pounds-32 Pounds lbs",
        "5 Pounds-30 Pounds lbs",
        "5 Pounds-32 Pounds lbs",
        "6 Pounds-30 Pounds lbs",
        "6 Pounds-40 Pounds lbs",
        "5 Pounds-35 Pounds lbs",
        "4 Pounds-35 Pounds lbs",
        "20 Pounds-40 Pounds lbs",
        "3 Kilograms-54 Kilograms lbs",
        "3 Kilograms-65 Pounds lbs",
        "2.2 Pounds-45 Pounds lbs",
        "2.3 Kilograms-10 Kilograms lbs",
        "1.8 Kilograms-10 Kilograms lbs"
    ],

    # Cluster 4 — Toddler–Youth Ranges
    "3": [
        "5 Pounds-40 Pounds lbs",
        "5 Pounds-50 Pounds lbs",
        "4 Pounds-50 Pounds lbs",
        "5 Pounds-55 Pounds lbs",
        "16 Pounds-50 Pounds lbs",
        "20 Pounds-50 Pounds lbs",
        "22 Pounds-50 Pounds lbs",
        "20 Pounds-65 Pounds lbs",
        "5 Pounds-65 Pounds lbs",
        "4 Pounds-65 Pounds lbs",
        "6 Pounds-65 Pounds lbs",
        "14 Pounds-65 Pounds lbs",
        "5 Kilograms-65 Kilograms lbs"
    ],

    # Cluster 5 — Youth–Booster Ranges (~80–110 lb)
    "4": [
        "5 Pounds-80 Pounds lbs",
        "22 Pounds-80 Pounds lbs",
        "5 Pounds-80 Pounds, 50 Pounds lbs",
        "40 Pounds-100 Pounds lbs",
        "20 Pounds-100 Pounds lbs",
        "22 Pounds-100 Pounds lbs",
        "25 Pounds-100 Pounds lbs",
        "30 Pounds-100 Pounds lbs",
        "5 Pounds-100 Pounds lbs",
        "4 Pounds-100 Pounds lbs",
        "40 Pounds-110 Pounds lbs",
        "5 Pounds-110 Pounds lbs",
        "22 Pounds-110 Pounds lbs",
        "33.1 Pounds-79.4 Pounds lbs",
        "5 Pounds-88.18 Pounds lbs"
    ],

    # Cluster 6 — High-Capacity Booster (≈100–120 lb+)
    "5": [
        "5 Pounds-120 Pounds lbs",
        "4 Pounds-120 Pounds lbs",
        "40 Pounds-120 Pounds lbs",
        "20 Pounds-120 Pounds lbs",
        "22 Pounds-120 Pounds lbs",
        "25 Pounds-120 Pounds lbs",
        "5.5 Pounds-120 Pounds lbs",
        "5 Pounds-65 Pounds, 120 Pounds, 50 Pounds lbs",
        "40 Pounds-40 Pounds, 100 Pounds lbs"
    ],

    # Cluster 7 — Kilogram-Based Ranges
    "6": [
        "18.1 Kilograms-49.8 Kilograms lbs",
        "18.1 Kilograms-49.9 Kilograms lbs",
        "2.3 Kilograms-18 Kilograms lbs",
        "2.3 Kilograms-10 Kilograms lbs",
        "2300 Grams-10000 Grams lbs"
    ],

    # Cluster 8 — Outliers / Malformed
    "7": [
        "40 Pounds",
        "22 Pounds-8 Pounds lbs",
        "5 Pounds-40 Grams lbs",
        "4 Pounds-20 Grams lbs",
        "csv_na",
        # below are the abnormals
        "5 Pounds-18 Kilograms lbs",
        "4 Pounds-70 Pounds lbs",
        "4 Pounds-45 Pounds lbs",
        "5 Pounds-70 Pounds lbs",
        "15 Kilograms-100 Pounds lbs",
        "4 Pounds-40 Pounds lbs",
        "18.14 Kilograms-49.9 Kilograms lbs",
        "5 Pounds-22 Pounds lbs",
        "5 Pounds",
        "33 Pounds-33 Pounds lbs",
    ]
    },

    #--------------------------------------------------------
    "Installation Type" : {
    #"latch_only": [
    "0": [
        "Latch",
        "Latch Belt"
    ],
    #"seat_belt_only": [
    "1": [
        "Seat Belt",
        "Seat",
        "Belt Positioning",
        "Seat With Base"
    ],
    #"latch_and_seat_belt": [
    "2": [
        "Seat Belt, Latch",
        "Seatbelt,Latch",
        "Seat Belt/Latch",
        "Latch, Seat Belt",
        "Latch or Seat Belt",
        "Seat Belt,Latch",
        "Seat belt and auto retracting LATCH"
    ],
    #"clicktight": [
    "3": [
        "Clicktight",
        "Clicktight Installation"
    ],
    #"special_other": [
    "4": [
        "Tabletop",
        "Snaps",
        "Parkway",
        "Text-align",
        "csv_na",
    ]
    },

    "Harness Type" : {
    #"five_point_harness": [
    "0": [
        "5 pt",
        "5-Point"
    ],
    #"three_point_harness": [
    "1": [
        "3-Point",
        "3-point harness"
    ],
    #"no_harness": [
    "2": [
        "No harness",
        "csv_na",
    ],
    #"vehicle_seat_belt": [
    "3": [
        "Seat Belt",
        "Vehicle seat belt"
    ]
    },

    "Material" : {
    #"foam": [
    "0": [
        "Plush, Foam",
        "Memory Foam",
        "foam,steel",
        "foam",
        "Fabric and foam",
        "Foam, Metal",
        "Foam, Alloy Steel, Plastic",
        "Foam,polyester",
        "Foam",
        "Ethylene Vinyl Acetate Foam Pad",
        "memory foam",
        "Foam,Steel",
        "Foam and fabric",
        "foam, Plastic",
        "Steel, fabric, foam, plush",
        "Foam,Polyester",
        "Polyester, Foam, Alloy Steel, Plastic",
        "Polyester, Foam, Plastic, Metal",
        "Foam,steel",
    ],
    #"textile": [
    "1": [
        "Polyester Blend",
        "Polyester,bamboo,rayon",
        "Fabric",
        "Fabric,Plush",
        "Bamboo",
        "Bamboo,rayon",
        "jersey,fabric",
        "Jersey,fabric",
        "Jersey,Fabric",
        "fabric",
        "Plush",
        "plush",
        "Polyester, Cotton",
        "Wool",
        "Wool Blend, Alloy Steel, Plastic",
        "Nylon",
        "Polyester",
        "Polyester, Polypropylene, Cotton"
    ],
    #"plastic": [
    "2": [
        "plastic",
        "Polyester, Plastic",
        "Abs plastic",
        "Plastic, Metal, Fabric",
        "Foam, Plastic",
        "Plastic, Metal",
        "Plastic",
        "Polypropylene",
        "High Density Polyethylene",
        "Polypropylene, High Density Polyethylene, Metal",
        "High Density Polyethylene, Polypropylene, Metal"
    ],
    #"metal": [
    "3": [
        "Metal",
        "Alloy Steel",
        "Alloy Steel, Polypropylene, Plastic, Polystyrene",
        "Steel",
        "Iron",
        "Aluminum",
        "Aluminum Alloy Seat Frame With Mesh Seat",
        "metall",
        "Alloy Steel, Plastic",
        "Foam, Alloy Steel",
        "Foam,Metal,Steel",
        "Steel, fabric, foam, plush",
        "Wool Blend, Alloy Steel, Plastic",
        "Polyester, Alloy Steel, Plastic",
        "Polyester, Metal"
    ],
    #"leather": [
    "4": [
        "Leather",
        "leather, vinyl or cloth seats."
    ],
    #"mixed_other": [
    "5": [
        "Polyester, Foam, Plastic, Metal",
        "Metal, Fabric, Plastic",
        "Steel, fabric, foam, plush, Plastic",
        "mica",
        "Pearl",
        "triton",
        "Glass",
        "csv_na"
    ]
    },


}