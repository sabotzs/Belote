from card import list_of_faces

def get_face_index(card):
    for i in range(len(list_of_faces)):
        if card.face == list_of_faces[i]:
            return i

def sort_part_by_face(part):
    for i in range(len(part)-1):
        current_idx = i
        for j in range(i+1,len(part)):
            current_face_idx = get_face_index(part[current_idx])
            j_face_idx = get_face_index(part[j])

            if current_face_idx > j_face_idx:
                current_idx=j
        part[current_idx], part[i] = part[i], part[current_idx]
    return part

def sort_hand_by_face(helper, hand, first_idx, second_idx):
    if first_idx >= len(hand):
        return
    while second_idx < len(hand) and hand[first_idx].suit == hand[second_idx].suit:
        second_idx +=1
    part = sort_part_by_face(hand[first_idx:second_idx])
    helper.append(part)
    sort_hand_by_face(helper,hand,second_idx,second_idx+1)

# def reduce(lists):
#     result = []
#     for lst in lists:
#         for el in lst:
#             result.append(el)
#     return result

def sort_hand(hand):
    hand = sorted(hand, key=lambda e : e.suit)
    helper = []
    sort_hand_by_face(helper,hand,0,1)
    return helper