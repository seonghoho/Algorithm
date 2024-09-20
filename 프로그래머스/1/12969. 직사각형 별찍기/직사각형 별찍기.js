process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    const n = data.split(" ");
    const a = Number(n[0]), b = Number(n[1]);
    
    let lst = ''
    for (let i=0; i< a; i++) {
        lst += '*'
    }
    cnt = 0
    while (cnt <b) {
        console.log(lst)
        cnt++
    }
});