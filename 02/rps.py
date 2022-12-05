class RPS:
    def __init__(self, opponent_choice) -> None:
        self.opponent_choice = opponent_choice
        pass
    
    def get_lose_choice(self):
        match self.opponent_choice:
            case 'A':
                return 'C'
            case 'B':
                return 'A'
            case 'C':
                return 'B'
        
    def get_draw_choice(self):
        return self.opponent_choice
            
    def get_win_choice(self):
        match self.opponent_choice:
            case 'A':
                return 'B'
            case 'B':
                return 'C'
            case 'C':
                return 'A'
        