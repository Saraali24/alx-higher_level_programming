#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to list
 * Return: 0
 */
int check_cycle(listint_t *list)
{
if (list->next)
return (1);
return (0);
}
