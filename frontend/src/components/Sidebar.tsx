
import { NavLink } from "react-router-dom"
import { LayoutDashboard, Users, BookOpen, CalendarCheck, BarChart3, LogOut } from "lucide-react"
import { cn } from "../lib/utils"

interface SidebarProps {
  role: "admin" | "lecturer" | "student"
}

export function Sidebar({ role }: SidebarProps) {
  const navItems = {
    admin: [
      { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
      { name: "Students", href: "/students", icon: Users },
      { name: "Courses", href: "/courses", icon: BookOpen },
      { name: "Reports", href: "/reports", icon: BarChart3 },
    ],
    lecturer: [
      { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
      { name: "My Courses", href: "/courses", icon: BookOpen },
      { name: "Mark Attendance", href: "/attendance", icon: CalendarCheck },
      { name: "Reports", href: "/reports", icon: BarChart3 },
    ],
    student: [
      { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
      { name: "My Courses", href: "/courses", icon: BookOpen },
      { name: "My Attendance", href: "/attendance-history", icon: CalendarCheck },
    ]
  }

  const items = navItems[role] || navItems.student

  return (
    <div className="flex h-full w-64 flex-col border-r bg-card px-4 py-6 text-card-foreground shadow-sm">
      <div className="flex items-center gap-2 px-2 mb-8 text-primary">
        <div className="flex h-8 w-8 items-center justify-center rounded-md bg-primary text-primary-foreground">
          <CalendarCheck size={20} />
        </div>
        <span className="text-lg font-bold tracking-tight text-foreground">NexusEdu</span>
      </div>
      
      <nav className="flex-1 space-y-1">
        {items.map((item) => (
          <NavLink
            key={item.name}
            to={item.href}
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-colors",
                isActive 
                  ? "bg-primary text-primary-foreground" 
                  : "text-muted-foreground hover:bg-muted hover:text-foreground"
              )
            }
          >
            <item.icon size={18} />
            {item.name}
          </NavLink>
        ))}
      </nav>

      <div className="mt-auto border-t pt-4">
        <NavLink
          to="/login"
          className="flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-destructive hover:text-destructive-foreground"
        >
          <LogOut size={18} />
          Logout
        </NavLink>
      </div>
    </div>
  )
}
