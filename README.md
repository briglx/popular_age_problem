# Popular Age Problem

There is a incredibly terribly neat riddle that goes:

> Two old friends, Jack and Bill, meet after a long time.
>
> Three kids
>
> Jack: Hey, how are you, man?
>
> Bill: Not bad, got married and I have three kids now.
>
> Jack: That's awesome. How old are they?
>
> Bill: The product of their ages is 72 and the sum of their ages is the same as your birth date.
>
> Jack: Cool..But I still don't know.
>
> Bill: My eldest kid just started taking piano lessons.
>
> Jack: Oh, now I get it.
>
>
> How old are Bill's kids?

What do we know?

- Three kids with unknown ages (a, b, c)
- Age product is `a*b*c* = 72`
- Birthdate is `dd` and `< 31`
- Age sum is `a+b+c is between [1-31]`

Only the following combinations have a product of 72:

| Ages | Product | Sum |
|------|---------|-----|
| (1, 1, 72) | 72 | 74 |
| (1, 2, 36) | 72 | 39 |
| (1, 3, 24) | 72 | 28 |
| (1, 4, 18) | 72 | 23 |
| (1, 6, 12) | 72 | 19 |
| (1, 8, 9) | 72 | 18 |
| (2, 2, 18) | 72 | 22 |
| (2, 3, 12) | 72 | 17 |
| (2, 4, 9) | 72 | 15 |
| (2, 6, 6) | 72 | 14 |
| (3, 3, 8) | 72 | 14 |
| (3, 4, 6) | 72 | 13 |

We can limit further where sum is less than 31:

| Ages | Product | Sum |
|------|---------|-----|
| (1, 3, 24) | 72 | 28 |
| (1, 4, 18) | 72 | 23 |
| (1, 6, 12) | 72 | 19 |
| (1, 8, 9) | 72 | 18 |
| (2, 2, 18) | 72 | 22 |
| (2, 3, 12) | 72 | 17 |
| (2, 4, 9) | 72 | 15 |
| (2, 6, 6) | 72 | 14 |
| (3, 3, 8) | 72 | 14 |
| (3, 4, 6) | 72 | 13 |

Only One sum where Jack didn't have enough information and needed one more quess

| Ages | Product | Sum |
|------|---------|-----|
| (2, 6, 6) | 72 | 14 |
| (3, 3, 8) | 72 | 14 |

Oldest staring piano gives the oldest is not a twin

| Ages | Product | Sum |
|------|---------|-----|
| (3, 3, 8) | 72 | 14 |
