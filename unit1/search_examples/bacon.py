import json

def make_actor_dictionary(data):
    acted_with = {}
    for pair in data:
        actor0 = pair[0]
        actor1 = pair[1]
        if actor0 not in acted_with:
            acted_with[actor0] = set()
        if actor1 not in acted_with:
            acted_with[actor1] = set()
        acted_with[actor0].add(actor1)
        acted_with[actor1].add(actor0)
    return acted_with

def did_x_and_y_act_together(data, actor_id_0, actor_id_1):
    acted_with = make_actor_dictionary(data)
    return actor_id_1 in acted_with[actor_id_0] or actor_id_0 in acted_with[actor_id_1]

def get_actors_with_bacon_number(data, bacon_number):
    acted_with = make_actor_dictionary(data)
    queue = [(4724,0)]
    visited = set()
    result = set()
    while len(queue) > 0:
        id, bn = queue.pop(0)
        if id not in visited:
            visited.add(id)
            if bn == bacon_number:
                result.add(id)
            else:
                for actor in acted_with[id]:
                    queue.append((actor, bn+1))
    return result


def get_bacon_path(data, actor_id):
    acted_with = make_actor_dictionary(data)
    queue = [[4724]]
    visited = set()
    while queue:
        partial_path = queue.pop(0)
        if partial_path[-1] == actor_id:
            return partial_path
        curr_id = partial_path[-1]
        if curr_id not in visited:
            visited.add(curr_id)
            for actor in acted_with[curr_id]:
                queue.append(partial_path + [actor])
    return []

def get_path(data, actor_id_0, actor_id_1):
    acted_with = make_actor_dictionary(data)
    queue = [[actor_id_0]]
    visited = set()
    while queue:
        partial_path = queue.pop(0)
        if partial_path[-1] == actor_id_1:
            return partial_path
        curr_id = partial_path[-1]
        if curr_id not in visited:
            visited.add(curr_id)
            for actor in acted_with[curr_id]:
                queue.append(partial_path + [actor])
    return []

# the three functions below this comment are fully optional - 
# feel free to do if you want! These are not tested with 
# test.py, so you won't be able to "check" that they're
# right in the same way.
def get_actor_path(path_of_ids):
    return []

def get_movie_path(movie_data, actor_data, actor_id_1, actor_id_2):
    return []

if __name__ == '__main__':
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    pass

