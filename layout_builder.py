def build_comic_layout(outline, story, image_paths):

    layout = []

    for i, panel in enumerate(outline):

        layout.append({
            "panel": panel["panel"],
            "title": panel["title"],
            "image": image_paths[i],
            "text": story
        })

    return layout