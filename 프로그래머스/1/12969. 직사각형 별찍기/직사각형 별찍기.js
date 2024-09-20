process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    
    let lst = '*'.repeat(a)
    cnt = 0
    while (cnt <b) {
        console.log(lst)
        cnt++
    }
});