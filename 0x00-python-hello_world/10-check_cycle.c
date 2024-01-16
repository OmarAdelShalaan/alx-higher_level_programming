#include "lists.h"

/**
 * check_cycle - check cycle of a listint_t list
 * @list: pointer to head of list
 * Return: 0 not cycle 1 if it is cycle
 */
int check_cycle(listint_t *list)
{
        listint_t *current;
        listint_t *temp;
        int i;

        current = list;
        temp = list;
        while(current != NULL)
        {
                if(temp == current->next)
                {
                        return (1);
                }
                current = current->next;
        }
        return (0);
}