#$/bin/bash
#Arguments:
# $1 - original filename
# $2 - new filename
# $3 - new size
convert $1 -resize $3 $2
