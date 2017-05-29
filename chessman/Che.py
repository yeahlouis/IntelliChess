from ChessPiece import ChessPiece

class Che(ChessPiece):

    def get_image_file_name(self):
        if self.selected:
            if self.is_red:
                return "images/RRS.gif"
            else:
                return "images/BRS.gif"
        else:
            if self.is_red:
                return "images/RR.gif"
            else:
                return "images/BR.gif"


    def can_move(self, board, dx, dy):
        if dx != 0 and dy != 0:
            #print 'no diag'
            return False
        nx, ny = self.x + dx, self.y + dy
        if nx < 0 or nx > 8 or ny < 0 or ny > 9:
            return False
        if (nx, ny) in board.pieces:
            if board.pieces[nx, ny].is_red == self.is_red:
                #print 'blocked by yourself'
                return False
        cnt = self.count_pieces(board, self.x, self.y, dx, dy)
        # print 'cnt', cnt
        if (nx, ny) not in board.pieces:
            if cnt!= 0:
                #print 'blocked'
                return False
        else:
            if cnt != 0:
                #print 'cannot kill'
                return False
            # print 'kill a chessman'
        return True

    #below added by Fei Li

    def __init__(self, x, y, is_red):
        ChessPiece.__init__(self, x, y, is_red)
        self.name = 'Che'
        if self.is_red:
            self.ID = 6
        else:
            self.ID = 7

    def get_moves(self, board):
        moves = []
        dx = 0
        dy = 0
        while True:
            dy += 1
            nx = self.x + dx
            ny = self.y + dy
            if ny > 9:
                break
            if (nx, ny) not in board.pieces:
                moves.append((self.x, self.y, dx, dy))
            else:
                if board.pieces[nx, ny].is_red != self.is_red:
                    moves.append((self.x, self.y, dx, dy))
                break
        dx = 0
        dy = 0
        while True:
            dy -= 1
            nx = self.x + dx
            ny = self.y + dy
            if ny < 0:
                break
            if (nx, ny) not in board.pieces:
                moves.append((self.x, self.y, dx, dy))
            else:
                if board.pieces[nx, ny].is_red != self.is_red:
                    moves.append((self.x, self.y, dx, dy))
                break
        dx = 0
        dy = 0
        while True:
            dx += 1
            nx = self.x + dx
            ny = self.y + dy
            if nx > 8:
                break
            if (nx, ny) not in board.pieces:
                moves.append((self.x, self.y, dx, dy))
            else:
                if board.pieces[nx, ny].is_red != self.is_red:
                    moves.append((self.x, self.y, dx, dy))
                break
        dx = 0
        dy = 0
        while True:
            dx -= 1
            nx = self.x + dx
            ny = self.y + dy
            if nx < 0:
                break
            if (nx, ny) not in board.pieces:
                moves.append((self.x, self.y, dx, dy))
            else:
                if board.pieces[nx, ny].is_red != self.is_red:
                    moves.append((self.x, self.y, dx, dy))
                break
        return moves
