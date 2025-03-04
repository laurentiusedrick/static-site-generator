
def markdown_to_blocks(markdown):
  return list(filter(lambda y: y != '',map(lambda x: x.lstrip().rstrip(), markdown.split("\n\n"))))
