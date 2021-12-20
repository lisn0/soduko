:- use_module(library(bounds)).

sudoku4(Pss) :-
    flatten(Pss, Ps),
    Ps in 1..4,
    maplist(all_different, Pss),
    Pss = [R1,R2,R3,R4],
    columns(R1, R2, R3, R4),
    blocks(R1, R2), blocks(R3, R4),
    label(Ps).

columns([], [], [], []).
columns([A|As],[B|Bs],[C|Cs],[D|Ds]) :-
    all_different([A,B,C,D]),
    columns(As, Bs, Cs, Ds).

blocks([], []).
blocks([X1,X2|R1], [X3,X4|R2]) :-
    all_different([X1,X2,X3,X4]),
    blocks(R1, R2).