function longest_sequence(seq, elem), iter

input:
    seq: list of integers
    elem: target element

output:
    integer, longest consecutive sequence of elem in seq

var longest_sequence, set longest_sequence to 0
var current_sequence, set current_sequence to 0

for every element in list of integers
    if element is target element
        increment current_sequence by 1
        if current_sequence greater than longest_sequence
            set longest_sequence to current_sequence
        end if
    else
        set current_sequence to 0
    end if
end for
return longest_sequence

