<script>
    import {FilmStore} from '../../film-store'
</script>

<ul>
    {#each $FilmStore as film}
        <li>
            <a href="films/{film.id}">{film.name}</a>
        </li>
    {/each}
</ul>