
def preview(text):
    text = input()
    if len(text) > 124:
        return '...'
    else:
        return text
print(preview())