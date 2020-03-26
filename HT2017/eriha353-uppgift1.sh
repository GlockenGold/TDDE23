#!/bin/sh
if [ $3 = "A" ]
then
    if [ $4 -eq "1" ]
    then grep -v C1B schema.txt | grep -v "  C1A-[234]"
    elif [ $4 -eq "2" ]
    then grep -v C1B schema.txt | grep -v "C1A-[134]  "
    elif [ $4 -eq "3" ]
    then grep -v C1B schema.txt | grep -v "  C1A-[124]"
    elif [ $4 -eq "4" ]
    then grep -v C1B schema.txt | grep -v "C1A-[123]  "
    fi
elif [ $3 = "B" ]
then
    if [ $4 -eq "1" ]
    then grep -v C1A schema.txt | grep -v "  C1B-[234]"
    elif [ $4 -eq "2" ]
    then grep -v C1A schema.txt | grep -v "C1B-[134]  "
    elif [ $4 -eq "3" ]
    then grep -v C1A schema.txt | grep -v "  C1B-[124]"
    elif [ $4 -eq "4" ]
    then grep -v C1A schema.txt | grep -v "C1B-[123]  "
fi
