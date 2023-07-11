#include "lists.h"

/**
 * check_cycle - does the list contain a cycle?
 * @list: the list in question above
 * Return: 0 for no, 1 for yes
 */
int check_cycle(listint_t *list)
{
	listint_t *drag;
	listint_t *speed;

	drag = list;
	speed = list;

	if (list == NULL)
	{
		return (0);
	}
	for (; drag && speed && speed->next; drag = drag->next,
			speed = speed->next->next)
	{
		if (drag == speed)
		{
			return (1);
		}
	}
	return (0);
}
