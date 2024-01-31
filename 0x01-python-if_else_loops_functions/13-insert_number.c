#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node to a listint_t list
 * @head: pointer to head of list
 * @number: data will add
 * Return: number of nodes
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new;
        listint_t *current;

        current = *head;

        new = malloc(sizeof(listint_t));
        if (new == NULL)
                return (NULL);

        new->n = number;
        new->next = NULL;

        if (*head == NULL)
                *head = new;
        else
        {
                while (current->next != NULL)
                {
                        if (current->n < number)
                                current = current->next;
                        else
                        {
                                new->next = current->next;
                                break;
                        }
                }
                current->next = new;
        }

        return (new);
}