import {writable} from 'svelte/store' 

export const FilmStore = writable([
    {id: 1, name: 'The Godfather', director: 'Francis Ford Coppola'},
    {id: 2, name: "The Big Lebowski", director: "Coen Brothers"},
])