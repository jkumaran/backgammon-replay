import json, re, copy

moves_raw = [
  { 'p': 'cameronwhale', 'm': '6 ➡ 3 , 8 ➡ 3', 'd': True, 't': '9/19/2026 07:41 AM', 'hit': False },
  { 'p': '-George', 'm': '6 ➡ 4 , 6 ➡ 4 , 13 ➡ 11 , 13 ➡ 11', 'd': True, 't': '10:44 AM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '13 ➡ 7 , 13 ➡ 7 , 8 ➡ 2 , 8 ➡ 2', 'd': True, 't': '11:51 AM', 'hit': False },
  { 'p': '-George', 'm': '13 ➡ 8 , 8 ➡ 4', 'd': False, 't': '12:40 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '13 ➡ 7 , 7 ➡ 6', 'd': False, 't': '01:19 PM', 'hit': False },
  { 'p': '-George', 'm': '8 ➡ 3 , 6 ➡ 3', 'd': False, 't': '06:50 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '6 ➡ 5 , 6 ➡ 5 , 24 ➡ 23 , 24 ➡ 23', 'd': True, 't': '08:08 PM', 'hit': False },
  { 'p': '-George', 'm': '11 ➡ 5 , 5 ➡ 3', 'd': False, 't': '08:29 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '13 ➡ 7 , 13 ➡ 8', 'd': False, 't': '08:32 PM', 'hit': False },
  { 'p': '-George', 'm': '13 ➡ 12 , 12 ➡ 11 , 13 ➡ 12 , 12 ➡ 11', 'd': True, 't': '08:39 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '23 ➡ 18 , 18 ➡ 16', 'd': False, 't': '10:04 PM', 'hit': False },
  { 'p': '-George', 'm': '11 ➡ 5 , 5 ➡ 1', 'd': False, 't': '9/20/2026 12:08 AM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '16 ➡ 15 , 15 ➡ 13', 'd': False, 't': '03:40 AM', 'hit': False },
  { 'p': '-George', 'm': '11 ➡ 5 , 5 ➡ 1', 'd': False, 't': '03:48 AM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '23 ➡ 18 , 8 ➡ 7', 'd': False, 't': '08:34 AM', 'hit': False },
  { 'p': '-George', 'm': '11 ➡ 7 (hitting) , 3 ➡ 1', 'd': False, 't': '08:53 AM', 'hit': True },
  { 'p': '-George', 'm': '8 ➡ 3 , 8 ➡ 3 , 6 ➡ 1 , 6 ➡ 1', 'd': True, 't': '08:53 AM', 'hit': False },
  { 'p': '-George', 'm': '7 ➡ 2 , 4 ➡ 2', 'd': False, 't': '08:54 AM', 'hit': False },
  { 'p': '-George', 'm': '4 ➡ 2 , 4 ➡ 3', 'd': False, 't': '04:34 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': 'bar ➡ 20 , 7 ➡ 4', 'd': False, 't': '04:34 PM', 'hit': False },
  { 'p': '-George', 'm': '3 ➡ 1 , 3 ➡ 2', 'd': False, 't': '04:35 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '4 ➡ 3 , 20 ➡ 16', 'd': False, 't': '04:35 PM', 'hit': False },
  { 'p': '-George', 'm': '3 ➡ 1', 'd': False, 't': '10:58 PM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '13 ➡ 12 , 12 ➡ 11 , 16 ➡ 15 , 15 ➡ 14', 'd': True, 't': '9/21/2026 07:45 AM', 'hit': False },
  { 'p': '-George', 'm': '24 ➡ 21 , 3 ➡ 1', 'd': False, 't': '07:49 AM', 'hit': False },
  { 'p': 'cameronwhale', 'm': '7 ➡ 4 (hit) , 4 ➡ 1 (hit) , 7 ➡ 4 , 4 ➡ 1', 'd': True, 't': '07:50 AM', 'hit': True },
  { 'p': 'cameronwhale', 'm': '7 ➡ 5 , 14 ➡ 9', 'd': False, 't': '07:51 AM', 'hit': False }
]

def parse_submoves(m_str):
    parts = m_str.split(',')
    res = []
    for p in parts:
        p = p.strip()
        m = re.search(r'(bar|\d+)\s*➡\s*(\d+|off)', p)
        if m:
            s, d = m.group(1), m.group(2)
            res.append((s, d, p))
    return res

def calc_pips(cb, cbar, gb, gbar):
    cp = cbar * 25 + sum(i * cnt for i, cnt in cb.items())
    gp = gbar * 25 + sum((25 - i) * cnt for i, cnt in gb.items())
    return cp, gp

c_b = {i: 0 for i in range(1, 25)}
g_b = {i: 0 for i in range(1, 25)}
c_b[24] = 2; c_b[13] = 5; c_b[8] = 3; c_b[6] = 5
g_b[1] = 2; g_b[12] = 5; g_b[17] = 3; g_b[19] = 5
c_bar, g_bar = 0, 0
c_off, g_off = 0, 0

initial_state = {
    'cameron_board': copy.copy(c_b),
    'george_board': copy.copy(g_b),
    'cameron_bar': c_bar,
    'george_bar': g_bar,
    'cameron_off': c_off,
    'george_off': g_off,
    'cameron_pips': 167,
    'george_pips': 167
}

turns_data = []

for idx, move in enumerate(moves_raw):
    player = move['p']
    raw_sub = parse_submoves(move['m'])
    
    submoves = []
    dice_used = []
    
    for s_raw, d_raw, text in raw_sub:
        hit_occurred = False
        hit_player = None
        hit_point = None
        
        state_before = {
            'cameron_board': copy.copy(c_b),
            'george_board': copy.copy(g_b),
            'cameron_bar': c_bar,
            'george_bar': g_bar,
            'cameron_off': c_off,
            'george_off': g_off,
            'cameron_pips': calc_pips(c_b, c_bar, g_b, g_bar)[0],
            'george_pips': calc_pips(c_b, c_bar, g_b, g_bar)[1]
        }
        
        if player == 'cameronwhale':
            if s_raw == 'bar':
                from_abs = 'bar_c'
                c_bar -= 1
                dice_val = 25 - int(d_raw)
            else:
                from_abs = int(s_raw)
                c_b[from_abs] -= 1
                dice_val = from_abs - int(d_raw)
            dice_used.append(dice_val)
            
            if d_raw == 'off':
                to_abs = 'off_c'
                c_off += 1
            else:
                to_abs = int(d_raw)
                if g_b[to_abs] > 0:
                    g_b[to_abs] = 0
                    g_bar += 1
                    hit_occurred = True
                    hit_player = '-George'
                    hit_point = to_abs
                c_b[to_abs] += 1
        else: # -George
            if s_raw == 'bar':
                from_abs = 'bar_g'
                g_bar -= 1
                dice_val = 25 - int(d_raw)
            else:
                s_g = int(s_raw)
                from_abs = 25 - s_g
                g_b[from_abs] -= 1
                dice_val = s_g - int(d_raw)
            dice_used.append(dice_val)
            
            if d_raw == 'off':
                to_abs = 'off_g'
                g_off += 1
            else:
                d_g = int(d_raw)
                to_abs = 25 - d_g
                if c_b[to_abs] > 0:
                    c_b[to_abs] = 0
                    c_bar += 1
                    hit_occurred = True
                    hit_player = 'cameronwhale'
                    hit_point = to_abs
                g_b[to_abs] += 1
                
        cp, gp = calc_pips(c_b, c_bar, g_b, g_bar)
        
        submoves.append({
            'from_raw': s_raw,
            'to_raw': d_raw,
            'from_abs': from_abs,
            'to_abs': to_abs,
            'dice': dice_val,
            'hit': hit_occurred,
            'hit_player': hit_player,
            'hit_point': hit_point,
            'text': text,
            'state_before': state_before,
            'state_after': {
                'cameron_board': copy.copy(c_b),
                'george_board': copy.copy(g_b),
                'cameron_bar': c_bar,
                'george_bar': g_bar,
                'cameron_off': c_off,
                'george_off': g_off,
                'cameron_pips': cp,
                'george_pips': gp
            }
        })
        
    cp, gp = calc_pips(c_b, c_bar, g_b, g_bar)
    turns_data.append({
        'move_index': idx + 1,
        'player': player,
        'time': move['t'],
        'desc': move['m'],
        'is_double': move['d'],
        'has_hit': move['hit'],
        'dice': dice_used,
        'submoves': submoves,
        'state_after': {
            'cameron_board': copy.copy(c_b),
            'george_board': copy.copy(g_b),
            'cameron_bar': c_bar,
            'george_bar': g_bar,
            'cameron_off': c_off,
            'george_off': g_off,
            'cameron_pips': cp,
            'george_pips': gp
        }
    })

game_data = {
    'meta': {
        'table_id': '917860648',
        'progression': '59%',
        'total_moves': len(turns_data),
        'players': {
            'cameronwhale': {
                'name': 'cameronwhale',
                'color': '#f59e0b',
                'accent': '#fbbf24',
                'label': 'Cameron',
                'direction': '24 ➡ 1'
            },
            '-George': {
                'name': '-George',
                'color': '#10b981',
                'accent': '#34d399',
                'label': 'George',
                'direction': '1 ➡ 24'
            }
        }
    },
    'initial_state': initial_state,
    'turns': turns_data
}

with open('/Users/kumaran/Downloads/backgammon/game_data.json', 'w') as f:
    json.dump(game_data, f, indent=2)

print('Successfully generated game_data.json!')
