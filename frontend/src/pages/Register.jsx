import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import AuthLayout from '../components/AuthLayout';
import { authError } from '../services/authError';
import { User, Mail, Lock, Loader2, UserPlus, AlertCircle, CheckCircle } from 'lucide-react';

const Register = () => {
  const { register } = useAuth();
  const navigate = useNavigate();

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState('Client'); // Default role

  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);
    setIsSubmitting(true);

    try {
      await register(name, email, password, role);
      setSuccess(true);
      setTimeout(() => {
        navigate('/login');
      }, 2000);
    } catch (err) {
      console.error(err);
      setError(authError(err, 'Failed to register account. Please check your inputs and try again.'));
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <AuthLayout>
      <div className="auth-container">
        {/* Logo / Branding */}
        <div className="auth-title">
          <div className="auth-symbol">
            <UserPlus  />
          </div>
          <h1 >
            Create an account
          </h1>
          <p >
            Join ClientHub and start collaborating
          </p>
        </div>

        {/* Card */}
        <div className="auth-card">
          {error && (
            <div className="auth-alert" role="alert">
              <AlertCircle className="w-5 h-5 shrink-0 mt-0.5" />
              <span>{error}</span>
            </div>
          )}

          {success && (
            <div className="auth-alert success" role="status">
              <CheckCircle className="w-5 h-5 shrink-0 mt-0.5" />
              <span>Account created successfully! Redirecting to login...</span>
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            {/* Full Name */}
            <div>
              <label htmlFor="name" >
                Full Name
              </label>
              <div className="auth-field">
                <div className="auth-field-icon">
                  <User className="w-5 h-5" />
                </div>
                <input
                  id="name"
                  autoComplete="name"
                  minLength={2}
                  maxLength={255}
                  type="text"
                  required
                  placeholder="John Doe"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  disabled={isSubmitting || success}

                />
              </div>
            </div>

            {/* Email Address */}
            <div>
              <label htmlFor="email" >
                Email Address
              </label>
              <div className="auth-field">
                <div className="auth-field-icon">
                  <Mail className="w-5 h-5" />
                </div>
                <input
                  id="email"
                  autoComplete="email"
                  type="email"
                  required
                  placeholder="name@company.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  disabled={isSubmitting || success}

                />
              </div>
            </div>

            {/* Password */}
            <div>
              <label htmlFor="password" >
                Password
              </label>
              <div className="auth-field">
                <div className="auth-field-icon">
                  <Lock className="w-5 h-5" />
                </div>
                <input
                  id="password"
                  autoComplete="new-password"
                  minLength={6}
                  maxLength={72}
                  type="password"
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  disabled={isSubmitting || success}

                />
              </div>
            </div>

            {/* Role Selection */}
            <div>
              <label htmlFor="role" >
                I am a...
              </label>
              <select
                id="role"
                value={role}
                onChange={(e) => setRole(e.target.value)}
                disabled={isSubmitting || success}

              >
                <option value="Client">Client / External Partner</option>
                <option value="Team Member">Team Member / Agent</option>
                <option value="Admin">Administrator</option>
              </select>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={isSubmitting || success}
              className="auth-submit"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-5 h-5 animate-spin" />
                  <span>Registering...</span>
                </>
              ) : (
                <span>Register</span>
              )}
            </button>
          </form>

          {/* Bottom link */}
          <div className="auth-switch">
            Already have an account?{' '}
            <Link to="/login" >
              Sign in
            </Link>
          </div>
        </div>
      </div>
    </AuthLayout>
  );
};

export default Register;
