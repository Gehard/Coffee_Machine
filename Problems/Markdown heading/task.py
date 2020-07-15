def heading(string, markdown_level=1):
    if markdown_level < 1:
        markdown_level = 1
    elif markdown_level > 6:
        markdown_level = 6
    return f"{'#' * markdown_level} {string}"

