def calc_turn_cost(turn, history_mode, web_on, in_price, out_price, class_in, class_out):
    # history
    if history_mode == 'Last 3':
        hist_turns = min(turn - 1, 3)
    elif history_mode == 'Last 5':
        hist_turns = min(turn - 1, 5)
    else: # Full
        hist_turns = turn - 1
        
    hist_tokens = hist_turns * 260
    in_tokens = 500 + hist_tokens + 1250 + (800 if web_on else 0) + 80
    out_tokens = 180
    
    model_cost = (in_tokens * in_price + out_tokens * out_price) / 1000000.0
    web_cost = 0.008 if web_on else 0.0
    class_cost = (150 * class_in + 20 * class_out) / 1000000.0 if turn == 1 else 0.0
    
    return model_cost + web_cost + class_cost

def calc_conv_cost(turns, history_mode, web_on, in_price, out_price, class_in, class_out):
    return sum(calc_turn_cost(t, history_mode, web_on, in_price, out_price, class_in, class_out) for t in range(1, turns + 1))

configs = [
    {
        'name': 'Budget Bot',
        'in_p': 0.10, 'out_p': 0.40, 'c_in': 0.10, 'c_out': 0.40,
        'hist': 'Last 3',
        'web': {'Guide': False, 'Visa': False, 'Weather': False}
    },
    {
        'name': 'Smart Mix',
        'in_p': 0.30, 'out_p': 2.50, 'c_in': 0.10, 'c_out': 0.40,
        'hist': 'Last 5',
        'web': {'Guide': False, 'Visa': True, 'Weather': True}
    },
    {
        'name': 'Premium Concierge',
        'in_p': 5.00, 'out_p': 25.00, 'c_in': 0.30, 'c_out': 2.50,
        'hist': 'Full',
        'web': {'Guide': True, 'Visa': True, 'Weather': True}
    }
]

scenarios = [
    {
        'name': 'A (4 turns)', 'turns': 4,
        'mix': {'Guide': 0.50, 'Visa': 0.25, 'Weather': 0.10, 'Booking': 0.10, 'Complaint': 0.05},
        'vol': 300, 'days': 30
    },
    {
        'name': 'B (7 turns)', 'turns': 7,
        'mix': {'Guide': 0.30, 'Visa': 0.15, 'Weather': 0.10, 'Booking': 0.35, 'Complaint': 0.10},
        'vol': 1200, 'days': 30
    }
]

for c in configs:
    print('--- Config:', c['name'])
    for s in scenarios:
        cost_guide = calc_conv_cost(s['turns'], c['hist'], c['web']['Guide'], c['in_p'], c['out_p'], c['c_in'], c['c_out'])
        cost_visa = calc_conv_cost(s['turns'], c['hist'], c['web']['Visa'], c['in_p'], c['out_p'], c['c_in'], c['c_out'])
        cost_weather = calc_conv_cost(s['turns'], c['hist'], c['web']['Weather'], c['in_p'], c['out_p'], c['c_in'], c['c_out'])
        cost_handoff = (150 * c['c_in'] + 20 * c['c_out']) / 1000000.0
        
        avg_cost = (s['mix']['Guide'] * cost_guide + 
                    s['mix']['Visa'] * cost_visa + 
                    s['mix']['Weather'] * cost_weather + 
                    (s['mix']['Booking'] + s['mix']['Complaint']) * cost_handoff)
        
        monthly = avg_cost * s['vol'] * s['days']
        human = 0.50 * s['vol'] * s['days']
        savings = (human - monthly) / human * 100
        print(f"Scenario {s['name']}:")
        print(f"  avg_cost/conv: ${avg_cost:.5f}")
        print(f"  monthly: ${monthly:.2f}")
        print(f"  human: ${human:.2f}")
        print(f"  savings: {savings:.2f}%")
