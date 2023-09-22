-- Question 1a
scale_nums :: [Integer] -> Integer -> [Integer]
scale_nums list factor =
    map (\num -> num * factor) list

-- Question 1b
only_odds :: [[Integer]] -> [[Integer]]
only_odds list =
    filter (all (\num -> num `mod` 2 == 1)) list

-- Question 1c
largest :: String -> String -> String
largest first second =
    if length first >= length second then first else second

largest_in_list :: [String] -> String
largest_in_list [] = ""
largest_in_list (s:[]) = s
largest_in_list (s:xs) = largest s (largest_in_list xs)

-- Question 2a
count_if :: (a -> Bool) -> [a] -> Int
count_if predicate [] = 0
count_if predicate (x:xs)
    | predicate x = 1 + count_if predicate xs
    | otherwise = count_if predicate xs

-- Question 2b
count_if_with_filter :: (a -> Bool) -> [a] -> Int
count_if_with_filter predicate list =
    length (filter predicate list)

-- Question 2c
count_if_with_fold :: (a -> Bool) -> [a] -> Int
count_if_with_fold predicate list =
    foldl counter 0 list
    where
        counter accum item =
            if predicate item then
                1 + accum
            else
                accum

-- Question 3b
foo_original :: Integer -> Integer -> Integer -> (Integer -> a) -> [a]
foo_original x y z t = map t [x,x+z..y]

-- Notice that because currying is done under the hood in Haskell, the type
-- definition doesn't need to change when we do it ourselves. In fact, currying
-- gives us insight into the design choice behind writing the type definition as
-- a sequence delimited by ->, with no special treatment of the final return
-- type.
foo :: Integer -> Integer -> Integer -> (Integer -> a) -> [a]
foo x =
    (\y ->
        (\z ->
            (\t ->
                map t [x, x+z..y]
            )
        )
    )

-- Question 4

f a b =
    let c = \a -> a -- (1)
        d = \c -> b -- (2)
    in \e f -> c d e -- (3)


-- Question 6

data Triforce = Power | Courage | Wisdom

wielder :: Triforce -> String
wielder Power = "Ganon"
wielder Courage = "Link"
wielder Wisdom = "Zelda"

princess = wielder Wisdom

-- Question 6a
-- data InstagramUser = Influencer | Normie

-- Question 6b
-- lit_collab :: InstagramUser -> InstagramUser -> Bool
-- lit_collab Influencer Influencer = True
-- lit_collab _ _ = False

-- Question 6c
-- data InstagramUser = Influencer [String] | Normie

-- Question 6d
-- is_sponsor :: InstagramUser -> String -> Bool
-- is_sponsor Normie _ = False
-- is_sponsor (Influencer []) _ = False
-- is_sponsor (Influencer (x:xs)) sponsor =
--     sponsor == x || is_sponsor (Influencer xs) sponsor

-- Question 6e
data InstagramUser = Influencer [String] [InstagramUser] | Normie

-- Question 6f
count_influencers :: InstagramUser -> Integer
count_influencers Normie = 0
count_influencers (Influencer _ followers) = fromIntegral (length followers)

-- Question 7

data LinkedList = EmptyList | ListNode Integer LinkedList
    deriving Show

-- Question 7a
ll_contains :: LinkedList -> Integer -> Bool
ll_contains (EmptyList) _ = False
ll_contains (ListNode value list) num =
    num == value || ll_contains list num

-- Question 7b
ll_insert :: LinkedList -> Integer -> Integer -> LinkedList

-- Question 7c
-- Base case: an empty list will always become a list with the one given value.
ll_insert (EmptyList) _ num = ListNode num EmptyList
ll_insert (ListNode value tail) index num
    -- Base case: insert at head.
    | index <= 0 = ListNode num (ListNode value tail)
    -- Recursive case: rebuild the head and the result of recursing with
    -- (index-1), effectively "moving down" the list, using the tail as the next
    -- list to consider. Eventually the position we want will appear as the head
    -- and be caught at the base case.
    | otherwise = ListNode value (ll_insert tail (index-1) num)

-- Question 8b
longest_run :: [Bool] -> Integer
longest_run list =
    helper list 0 0
    where
        helper :: [Bool] -> Integer -> Integer -> Integer

        -- Base case: there's no more list left, so return the best we have.
        helper [] current_count current_max =
            max current_count current_max

        -- Current TRUE: take max(++count, current_max) and recurse with rest.
        helper (True:xs) current_count current_max =
            helper xs new_count new_max
            where
                new_count = current_count + 1
                new_max = max current_max new_count

        -- Current FALSE: reset current counter to 0 and recurse with rest.
        helper (False:xs) _ current_max =
            helper xs 0 current_max

-- Question 8d
data Tree = Empty | Node Integer [Tree]

max_tree_value :: Tree -> Integer
max_tree_value Empty = 0
max_tree_value (Node num []) = num
max_tree_value (Node num children) =
    max num children_max
    where
        children_max = maximum [max_tree_value child | child <- children]

-- Question 9
fibonacci :: Int -> [Int]
fibonacci n
    | n <= 0 = []
    | otherwise = [fib x | x <- [1..n]]
    where
        fib 1 = 1
        fib 2 = 1
        fib x = fib (x-1) + fib(x-2)

-- Question 10
data Event = Travel Integer | Fight Integer | Heal Integer

handle_events :: [Event] -> Integer -> Bool -> Integer
handle_events [] health _ =
    if health <= 0 then -1 else health

-- Small optimization such that we stop unnecessarily recursing once we reach -1
-- health, set by the fight handler.
handle_events _ (-1) _ = -1

handle_events ((Travel distance):xs) health defensive
    | defensive = handle_events xs health now_defensive
    | otherwise = handle_events xs new_health now_defensive
    where
        new_health = min 100 (health + distance `div` 4)
        now_defensive = new_health <= 40

handle_events ((Fight loss):xs) health defensive =
    if new_health <= 0
        then -1
        else handle_events xs new_health now_defensive
    where
        new_health =
            if defensive
                then health - loss `div` 2
                else health - loss
        now_defensive = new_health <= 40

handle_events ((Heal gain):xs) health defensive =
    handle_events xs new_health defensive
    where
        new_health = min 100 (health + gain)

super_giuseppe :: [Event] -> Integer
super_giuseppe events =
    handle_events events 100 False
