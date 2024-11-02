function solution(my_string, overwrite_string, s) {
    return my_string.slice(0,s).concat(overwrite_string).concat(my_string.slice(s+overwrite_string.length,my_string.length))
}