from enum import Enum
import re

class BlockType(Enum):
  PARAGRAPH = "paragraph"
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UL = "unordered_list"
  OL = "ordered_list"

def block_to_block_type(md_block):
 
  if len(re.findall(r"^#{1,6} .*", md_block)) > 0:
    return BlockType.HEADING
  
  if md_block.startswith("```") and md_block.endswith("```"):
    return BlockType.CODE
  
  if len(re.findall(r">.*", md_block)) == len(md_block.split("\n")):
    return BlockType.QUOTE
  
  if len(re.findall(r"\* .*|- .*", md_block)) == len(md_block.split("\n")):
    return BlockType.UL
  
  if len(re.findall(r"\d+. .*", md_block)) == len(md_block.split("\n")):
    return BlockType.OL
  
  return BlockType.PARAGRAPH