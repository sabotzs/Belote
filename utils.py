from card import list_of_faces

def get_face_index(card):
	for i in range(len(list_of_faces)):
		if card.face == list_of_faces[i]:
			return i

def sort_part_by_face(hand):
	for i in range(len(hand)-1):
		current_idx = i
		for j in range(i+1, len(hand)):
			current_face_idx = get_face_index(hand[current_idx])
			j_face_idx = get_face_index(hand[j])
			
			if current_face_idx > j_face_idx:
				current_idx = j
		hand[current_idx], hand[i] = hand[i], hand[current_idx]

	return hand

def sort_hand_by_face(hand, new_hand, first_idx, second_idx):
	if first_idx >= len(hand):
		return
	while second_idx < len(hand) and\
		hand[first_idx].suit == hand[second_idx].suit:
			second_idx += 1
	
	new_part = sort_part_by_face(hand[first_idx:second_idx])
	new_hand.append(new_part)
	sort_hand_by_face(hand, new_hand, second_idx, second_idx + 1)

# def reduce(lists):
# 	result = []
# 	for lst in lists:
# 		for el in lst:
# 			result.append(el)
# 	return result

def sort_hand(hand):
	hand = sorted(hand, key = lambda e: e.suit)
	parts = []
	sort_hand_by_face(hand, parts, 0, 1)
	return parts
	