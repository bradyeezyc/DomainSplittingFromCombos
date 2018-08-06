# DomainSplittingFromCombos
Splitting unique domains out of combo lists

## Background
 This was used to read 20+GB text files and process them, this is why mmap file reading approach has been used.
 
# Usage

```sh
python app.py -f filein.txt -o output.txt ([-d y] if you want debugging)
```

### File
Expecting the file to be in ```aaaaaaaaaaaa:bbbbbbbbb``` format

# Licence 

MIT
