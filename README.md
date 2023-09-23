# rpgfreedoc

Documentation generator for IBM's RPG Free language

Copyright 2023 [Jack J. Woehr](jwoehr@softwoehr.com)

Free and open source software. See LICENSE.

## Introduction

### Documentable comment

#### Comment block preceding declaration

An `rpgfreedoc` documentable comment consists of an RPG declaration preceded by a block of (possibly empty) consecutive comment lines, each line starting with slash-slash-space-opencurly:

`// {`

E.g.,

```rpg
// { myproc
// { arg1 ... something
// { arg2 ... something else
// { This proc does something with arg1 and arg 2
dcl-proc myproc
```

#### Relying on the IDE + editor pair

The IDE + editor pair should be extended to generate `rpgfreedoc` stub comment blocks. `rpgfreedoc` only translates comment-block / declaration pairs into data structures as input for creating an indexed human-readable document.

The author's intent is to add the ability to output formatted documentation from the aforementioned data structures.

### Work in progress

So far, the code can do the following:

```python
from rpgfreedoc import RPGFreeDocCommentBundler
x = RPGFreeDocCommentBundler.bundleFile('myfile.rpgle')
for key in x.__dict__.keys():
  for z in x.__dict__[key]:
    print(z.entity_line_number)
    print(z.entity)
    for q in z.comment_lines:
      print(q.line_number)
      print(q.comment_line)
```

Jack Woehr
2023-09-22
