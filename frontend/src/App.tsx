import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import { AuthGateway } from "./pages/AuthGateway"
import { DashboardLayout } from "./layouts/DashboardLayout"
import { AttendanceMarking } from "./pages/AttendanceMarking"

// Placeholders for other pages
const Placeholder = ({ title }: { title: string }) => (
  <div className="flex h-[60vh] flex-col items-center justify-center gap-4">
    <h1 className="text-2xl font-bold text-muted-foreground">{title} Component</h1>
    <p className="text-sm text-muted-foreground">This view is currently under development.</p>
  </div>
)

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<AuthGateway />} />
        
        {/* Dashboard Routes */}
        <Route element={<DashboardLayout />}>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/dashboard" element={<Placeholder title="Dashboard Overview" />} />
          <Route path="/students" element={<Placeholder title="Student Management" />} />
          <Route path="/courses" element={<Placeholder title="Course Management" />} />
          <Route path="/attendance" element={<AttendanceMarking />} />
          <Route path="/reports" element={<Placeholder title="Reports & Analytics" />} />
          <Route path="/attendance-history" element={<Placeholder title="My Attendance History" />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
