function generateBoard(size) {
    const board = [];
    for (let i = 0; i < size; i++) {
        const row = [];
        for (let j = 0; j < size; j++) {
            row.push(null);
        }
        board.push(row);
    }
    return board;
}

function checkWin(board, player) {
    const size = board.length;

    // Check rows
    for (let i = 0; i < size; i++) {
        let count = 0;
        for (let j = 0; j < size; j++) {
            if (board[i][j] === player) {
                count++;
                if (count === 5) return true;
            } else {
                count = 0;
            }
        }
    }

    // Check columns
    for (let j = 0; j < size; j++) {
        let count = 0;
        for (let i = 0; i < size; i++) {
            if (board[i][j] === player) {
                count++;
                if (count === 5) return true;
            } else {
                count = 0;
            }
        }
    }

    // Check diagonals (top-left to bottom-right)
    for (let k = -size + 1; k < size; k++) {
        let count = 0;
        for (let i = Math.max(0, k), j = Math.max(0, -k); i < size && j < size; i++, j++) {
            if (board[i][j] === player) {
                count++;
                if (count === 5) return true;
            } else {
                count = 0;
            }
        }
    }

    // Check diagonals (top-right to bottom-left)
    for (let k = 0; k < 2 * size - 1; k++) {
        let count = 0;
        for (let i = Math.max(0, k - size + 1), j = Math.min(size - 1, k); i < size && j >= 0; i++, j--) {
            if (board[i][j] === player) {
                count++;
                if (count === 5) return true;
            } else {
                count = 0;
            }
        }
    }

    return false;
}

// Example usage:
const boardSize = 15;
const board = generateBoard(boardSize);

function drawBoard(board) {
    txt = "<table>";
    
    for (let i = 0; i < board.length; i++) {
        txt += "<tr>";
        for (let j = 0; j < board[i].length; j++) {
            txt += `<td>${board[i][j] === null ? '.' : board[i][j]}</td>`;
        }
        txt += "</tr>";
        console.log(board[i].map(cell => cell === null ? '.' : cell).join(' '));

    }
    txt += "</table>";
    document.getElementById("board").innerHTML = txt;
}