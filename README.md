# Lab-7
## Description

Use python>=3.7 for run. Load crc, numpy, pandas libraries. 
At first program sum bytes of name and parameter, use CRC256 for hashing, mod numtickets.

## Usage
python3 lab7.py \<file> \<numtickets> \<parameter>
```
cd notes
python3 lab7.py "../input/input.csv" 100 41
```

## Input
 Иванов Иван Иванович
 
 Петров Петр Петрович
 
 Васильев Василий Васильевич
 
 Яров Ярослав Ярославович
 
 Дмитриев Дмитрий Дмитриевич
 
 Андреев Андрей Андреевич
 
 Никулин Николай Николаевич

## Output
 Иванов Иван Иванович: 27
 
 Петров Петр Петрович: 65
 
 Васильев Василий Васильевич: 91
 
 Яров Ярослав Ярославович: 31
 
 Дмитриев Дмитрий Дмитриевич: 63
 
 Андреев Андрей Андреевич: 96
 
 Никулин Николай Николаевич: 43
 
 Юрьев Юрий Юрьевич: 5
