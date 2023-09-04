#include "lists.h"

/**
 * check_cycle - checks whether a linked list is circular
 * @list: pointer to the list
 * Return: (int) 1 if circular, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
