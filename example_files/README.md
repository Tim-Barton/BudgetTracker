# Data Formats
## Configuration file
```
{  
"Categories": [  
  {
    "Category": <name of Category>, 
      "Regexes": [  
        <python re module compatible search strings>,  
        ...  
      ]
    },
    .....
  ],
  "Configuration": {
    "Spendfile": {
      "AmountIndex": <0 indexed int of column in data file for amount>,
      "DescriptionIndex": <0 indexed int of column in data file for description>,
      "SpendingIsNegative": <true/false depending on how your spend file denotes spent money>
      "DataType": <CSV is the only support data type at this point in time
    }
  }
}```

## Data file
Any comma delimited CSV will be read.  
The appropriate lines in the Configuration file denote which field 

## Notes
This assumes that you may be importing a Bank's transaction list that will have both spend amounts and your income amounts and need to distinguish between them.  

If you have two identical Regexes the program will use the second Category which lists it
