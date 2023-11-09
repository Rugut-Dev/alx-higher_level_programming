# C Doubly linked lists

## Learning Objectives

At the end of theis project, you are expectede to be able to explain to anyone, without the help of Google:

### General

* What is a doubly linked list
* How to use doubly linked list
* Understand and know to implement the various operations (deletion, insertion, etc) with doubly linked lists
* Start to look for the right source of information without too much help

## Tasks

#### 0. Print list
Write a function that prints all the elements of a dlistint_t list.

* Prototype: size_t print_dlistint(const dlistint_t *h);
* Return: the number of nodes
* Format: see example

#### 1. List Length
Write a function that returns the number of elements in a linked dlistint_t list.

* Prototype: size_t dlistint_len(const dlistint_t *h);

#### 2. Add node
Write a function that adds a new node at the beginning of a dlistint_t list.

* Prototype: dlistint_t *add_dnodeint(dlistint_t **head, const int n);
* Return: the address of the new element, or NULL if it failed

#### 3. Add node at the end
Write a function that adds a new node at the end of a dlistint_t list.

* Prototype: dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);
* Return: the address of the new element, or NULL if it failed

#### 4. Free list
Write a function that frees a dlistint_t list.

* Prototype: dlistint_t *add_dnodeint_end(dlistint_t **head, const int n);
* Return: the address of the new element, or NULL if it failed

#### 5. Get node at index
Write a function that returns the nth node of a dlistint_t linked list.

* Prototype: dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index);
* where index is the index of the node, starting from 0
* if the node does not exist, return NULL

#### 6. Sum list
Write a function that returns the sum of all the data (n) of a dlistint_t linked list.

* Prototype: int sum_dlistint(dlistint_t *head);
* if the list is empty, return 0

#### 7. Inset at index
Write a function that inserts a new node at a given position.

* Prototype: dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n);
* where idx is the index of the list where the new node should be added. Index starts at 0
* Returns: the address of the new node, or NULL if it failed
* if it is not possible to add the new node at index idx, do not add the new node and return NULL

#### 8. Write a function that deletes the node at index of a dlistint_t linked list.

* Prototype: int delete_dnodeint_at_index(dlistint_t **head, unsigned int index);
* where index is the index of the node that should be deleted. Index starts at 0
* Returns: 1 if it succeeded, -1 if it failed

#### Advanced Tasks