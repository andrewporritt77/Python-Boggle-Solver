def make_grid(width,height):
    """
    create grid to hold tiles for boggle game.
    """
    return{(row,col): ' ' for row in range(height)
        for col in range (width)
    }
    
