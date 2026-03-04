import React, { useEffect, useState } from "react"
import api from "../services/api"

export default function Dashboard() {
  const [tasks, setTasks] = useState<string[]>([])

  useEffect(() => {
    api.get("/tasks").then(res => setTasks(res.data.tasks))
  }, [])

  return (
    <div>
        <h1>Task Dashboard</h1>

      {tasks.map((t, i) => (
        <p key={i}>{t}</p>
      ))}
    </div>
  )
}