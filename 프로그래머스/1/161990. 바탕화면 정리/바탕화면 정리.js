function solution(wallpaper) {
    let startRow = wallpaper.length;
    let startCol = wallpaper[0].length;
    let endRow = 0;
    let endCol = 0;

    for (let i = 0; i < wallpaper.length; i++) {
        for (let j = 0; j < wallpaper[i].length; j++) {
            if (wallpaper[i][j] === '#') {
                if (i < startRow) startRow = i;
                if (j < startCol) startCol = j;
                if (i >= endRow) endRow = i + 1;
                if (j >= endCol) endCol = j + 1;
            }
        }
    }

    return [startRow, startCol, endRow, endCol];
}