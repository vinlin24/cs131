# 06/07


## Unification

Resolution *uses* unification.  Unification is a single operations that takes
`initial_mappings` and uses the matching rules on a goal tree and a fact/rule
tree.  Resolution is repeated application of
unification.

`W -> carey` is a match, but we DON'T output `W -> carey` because it's already
an existing mapping.  Unification as a single operation only outputs NEW
mappings, so in this case, an *empty* dictionary is returned.

Notice that `unify` returns a 2-tuple.  Why both returning a boolean WITH the
extracted mapping?  Why not just check that the extracted mapping is empty?
Because of the above case.  We can have a successful unification but return an
empty mapping i.e. `return (True, {})`.

---

**Arity** is the number of children of a goal tree in Prolog?  If arity doesn't
match, we automatically know the trees cannot match.

If an *unbound* variable and atom match, the variable is mapped to the atom e.g.
`Y -> carey`.

If an *unbound* variable matches another *unbound* variable, the variables are
bidirectionally mapped e.g. `Y <-> Z`.

**Unification *considers* the input `initial_mappings`, but only outputs NEW
mappings**

For example:

```
initial_mappings={W: carey}
goal=teach(W, cs131)
fact=teach(carey, cs131)
```

> Unification in a single sentence: "For any currently unbound variables, return
> the new bindings."


## Wacky List Operations

The general form of a list operation (e.g. deleting an atom from a list):

```prolog
delete(ItemToDelete, ListToDeleteFrom, ResultingList)
```

If we want the `ResultingList` to be outputted, then we just name it a variable
like `X` and let Prolog do its fill-in-the-blank magic.  If we don't have any
variables, we get a true/false output, which represents whether this is a valid
operation e.g. `append([1,2],[3,4],[1,2,3,4] -> true`.

Examples:

```
delete(carey, [paul, carey, david], X)
% X = [paul, david]
delete(carey, [paul, carey, david], [paul, david])
% true
```

Built-in list processing rules:

```prolog
append(X, Y, Z)
reverse(X, Y)
sort(X, Y)
member(X, Y)
permutation(X, Y)
sum_list(X, Y)
```

Remember that with all of these, the last variable represents the "resulting
list".

BTW, `[X|XS]` is syntactic sugar for normal functors and atoms:

```
[X|XS] -> cons(X, XS)
```

The empty list can be replaced with the atom `nil`.
