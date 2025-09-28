# questions_lighting.py
# Topic: Basic Lighting Styles (Art Quiz)

quiz_data = {
    "Basic Lighting Styles": {
        "easy": [
            {"question": "Which lighting style creates a triangle of light under the eye?\n a) Split\n b) Rembrandt\n c) Butterfly", "answer": "b"},
            {"question": "In Butterfly lighting, the shadow forms under which facial feature?\n a) Cheek\n b) Nose\n c) Chin", "answer": "b"},
            {"question": "Split lighting divides the face into which two parts?\n a) Light and shadow halves\n b) Diagonal sections\n c) Top and bottom", "answer": "a"},
            {"question": "In Loop lighting, the nose shadow points toward which facial feature?\n a) Chin\n b) Cheek\n c) Forehead", "answer": "b"},
            {"question": "Broad lighting emphasizes which side of the face?\n a) Narrow side\n b) Wider side\n c) Jawline", "answer": "b"},
            {"question": "Short lighting slims the face by highlighting which side?\n a) Wider side\n b) Narrow side\n c) Forehead", "answer": "b"},
            {"question": "Rim lighting is primarily used to separate the subject from which area?\n a) Foreground\n b) Background\n c) Shadows", "answer": "b"},
            {"question": "What is the main light in a three-point setup called?\n a) Fill\n b) Key\n c) Backlight", "answer": "b"},
            {"question": "High-key lighting is characterized by mostly what kind of tones?\n a) Shadows\n b) Bright tones\n c) Warm colors", "answer": "b"},
            {"question": "Chiaroscuro is a lighting technique that emphasizes what?\n a) Softness\n b) Contrast\n c) Color", "answer": "b"},
            {"question": "Which type of light is primarily used to reduce shadows?\n a) Highlights\n b) Fill light\n c) Key light", "answer": "b"},
            {"question": "Backlighting creates what kind of effect around the subject?\n a) Halo effect\n b) Split face\n c) Broad light", "answer": "a"},
            {"question": "What type of lighting device creates soft, diffused light?\n a) Harsh bulb\n b) Softbox\n c) Color gel", "answer": "b"},
            {"question": "At approximately what angle is Rembrandt lighting usually set?\n a) 90°\n b) 45°\n c) 180°", "answer": "b"},
            {"question": "Overhead lighting often creates which negative effect?\n a) Butterfly shadow\n b) Raccoon eyes\n c) Rim light", "answer": "b"},
            {"question": "What tool is used to bounce light back onto a subject?\n a) Light blocker\n b) Reflector\n c) Color filter", "answer": "b"},
            {"question": "Low-key lighting is primarily focused on creating what?\n a) Brightness\n b) Shadows\n c) Warmth", "answer": "b"},
            {"question": "A hair light is positioned to highlight which part of the subject?\n a) Forehead\n b) Shoulders\n c) Hair", "answer": "c"},
            {"question": "Loop lighting is considered a softer variation of which lighting style?\n a) Split\n b) Rembrandt\n c) Butterfly", "answer": "b"},
            {"question": "In Broad lighting, which side of the subject’s face is kept mostly shadow-free?\n a) Narrow side\n b) Wider side\n c) Nose", "answer": "b"}
        ],
        "medium": [
            {"question": "Which lighting style creates a triangle of light under the eye?", "answer": "Rembrandt"},
            {"question": "Which lighting style has a nose shadow that loops toward the cheek?", "answer": "Loop lighting"},
            {"question": "Which lighting style places the light directly in front and above the subject?", "answer": "Butterfly lighting"},
            {"question": "Which lighting style divides the face into equal light and shadow halves?", "answer": "Split lighting"},
            {"question": "Which lighting style highlights the edge of the subject?", "answer": "Rim lighting"},
            {"question": "What type of light is used to soften shadows from the key light?", "answer": "Fill light"},
            {"question": "Which type of lighting creates a halo effect behind the subject?", "answer": "Backlight"},
            {"question": "What lighting technique uses a single harsh light for drama?", "answer": "Chiaroscuro"},
            {"question": "Which lighting style produces bright, low-contrast illumination?", "answer": "High-key lighting"},
            {"question": "Which lighting emphasizes the broader side of the face?", "answer": "Broad lighting"},
            {"question": "Which lighting technique slims the face using shadows?", "answer": "Short lighting"},
            {"question": "Which tool provides diffused shadows?", "answer": "Softbox"},
            {"question": "Which tool redirects light onto the subject?", "answer": "Reflector"},
            {"question": "What is the lighting setup that uses key, fill, and backlight?", "answer": "Three-point"},
            {"question": "Which lighting style provides shadowless, even illumination?", "answer": "Flat lighting"},
            {"question": "Which technique emphasizes dramatic contrast between light and dark?", "answer": "Low-key lighting"},
            {"question": "Which type of light is placed behind and above the subject to add separation?", "answer": "Hair light"},
            {"question": "Which lighting style creates depth by blurring backgrounds?", "answer": "Atmospheric lighting"},
            {"question": "Which style of lighting uses mathematical placement such as a 45° angle?", "answer": "Rembrandt lighting"},
            {"question": "Which lighting style avoids shadows on the subject’s wider side?", "answer": "Broad lighting"}
        ],
        "hard": [
            {"question": "List the 3 lights used in a three-point setup.", "answer": "Key, Fill, Backlight"},
            {"question": "List 4 classic portrait lighting styles.", "answer": "Butterfly, Rembrandt, Split, Loop"},
            {"question": "List 3 common studio light sources.", "answer": "LED, Softbox, Fresnel"},
            {"question": "List 3 common light modifiers.", "answer": "Umbrella, Scrim, Diffuser"},
            {"question": "List 3 characteristics of Rembrandt lighting.", "answer": "Triangle under eye, 45° light, dramatic shadows"},
            {"question": "Explain how broad lighting differs from short lighting.", "answer": "Broad lights wider side; short lights narrower"},
            {"question": "List 3 steps to create Butterfly lighting.", "answer": "Front key light, position above, use reflector"},
            {"question": "List 3 challenges in lighting photography.", "answer": "Lens flare, underexposure, balancing light"},
            {"question": "List 3 benefits of using fill light.", "answer": "Reduce shadows, soften contrast, add detail"},
            {"question": "List 3 accessories used with lights.", "answer": "Barn doors, grids, beauty dishes"},
            {"question": "List 4 types of artificial light sources.", "answer": "Continuous, strobe, ring, LED panel"},
            {"question": "List 3 techniques for creating dramatic backlighting.", "answer": "Backlight, angle, low fill light"},
            {"question": "List 3 characteristics of high-key lighting.", "answer": "Brightness, minimal shadows, cheerful mood"},
            {"question": "Name the 2 categories of lighting quality.", "answer": "Hard, Soft"},
            {"question": "List 3 characteristics of Split lighting.", "answer": "Half light/half shadow, dramatic, side angle"},
            {"question": "List 2 adjustments to soften harsh shadows.", "answer": "Lower key light, use fill light"},
            {"question": "List 3 functions of a reflector.", "answer": "Bounce light, fill shadows, highlight hair"},
            {"question": "List 3 differences between continuous and flash lighting.", "answer": "Continuous vs. flash, heat, cost"},
            {"question": "List 4 characteristics of low-key lighting.", "answer": "Single light, high contrast, drama, depth"},
            {"question": "List 3 ways to soften light.", "answer": "Diffuser, bounce, increase fill light"}
        ]
    }
}