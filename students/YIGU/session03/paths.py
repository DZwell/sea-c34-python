def q():
    """# what happen when I have two files with the same name but different
    file type. I only call for the name of the file.
    I have two files ready in my folder. Both of them are 'secrets'.
    One file is txt and another is pdf."""
    import io
    f = io.open('secrets', encoding='utf-8')
    secret_data = f.read()
    print secret_data
    f.close()

    # Answer: Didn't error out. It read out of .txt.

q()
