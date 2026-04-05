import './App.css'
import TodoCard from "./components/todoCard.tsx";
import {useEffect, useState} from "react";

function App() {
    const [todos, setTodos] = useState([])

    useEffect(() => {
        const getData = async () => {
            const response = await fetch("http://127.0.0.1:8000/items")
            const data = await response.json()

            setTodos(data)
            console.log(data)
        }

        getData()
    }, [])

    async function addTodo(formData) {
        const todoText = formData.get("todoText")


        const response = await fetch("http://127.0.0.1:8000/items", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(
                {
                    text: todoText,
                    isDone: false
                }
            )
        })
        const saveTodo = await response.json()

        // @ts-ignore
        setTodos(prevState => [
            ...prevState,
            saveTodo
        ])
    }

    async function deleteTodo(id) {
        const response = await fetch(`http://127.0.0.1:8000/items/${id}`, {
            method: "DELETE"
        })

        if (response.ok) {
            setTodos(prevState => {
                return prevState.filter(todo => {
                    if (todo.id !== id)
                        return todo
                })
            })
        }
    }

    async function toggleTodo(id) {
        const todoToUpdate = todos.find(t => t.id === id);
        if (!todoToUpdate) return;

        const updatedTodo = {
            ...todoToUpdate,
            isDone: !todoToUpdate.isDone
        };

        // 3. Wyślij do bazy danych
        const response = await fetch(`http://127.0.0.1:8000/items/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(updatedTodo)
        });

        if (response.ok) {
            setTodos(prevState =>
                prevState.map(todo => (todo.id === id ? updatedTodo : todo))
            );
        }
    }

    return (
        <>
            <form action={addTodo}>
                <input name={"todoText"}/>
                <button type={"submit"}>Add todo</button>
            </form>
            {todos.map((todo) => {
                return <TodoCard
                    key={todo.id}
                    task={todo.text}
                    isDone={todo.isDone}
                    deleteFunction={() => deleteTodo(todo.id)}
                    toggleDone={() => toggleTodo(todo.id)}
                />
            })}
        </>
    )
}

export default App
