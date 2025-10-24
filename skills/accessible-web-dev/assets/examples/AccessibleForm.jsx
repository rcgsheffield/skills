import React, { useState } from 'react';

/**
 * Accessible Form Components
 *
 * Reusable form components that follow WCAG 2.1 AA standards:
 * - Proper label associations
 * - Error messaging with aria-live regions
 * - Required field indicators
 * - Clear focus states
 * - Validation feedback
 *
 * Components:
 * - FormField: Wrapper for form inputs with label and error handling
 * - TextInput: Accessible text input
 * - SelectInput: Accessible select dropdown
 * - CheckboxGroup: Accessible checkbox group
 * - RadioGroup: Accessible radio button group
 */

// FormField wrapper component
const FormField = ({ children, error, helpText }) => {
  return (
    <div className="form-field">
      {children}
      {helpText && !error && (
        <span className="help-text">{helpText}</span>
      )}
      {error && (
        <span className="error-message" role="alert">
          {error}
        </span>
      )}
      <style jsx>{`
        .form-field {
          margin-bottom: 20px;
        }

        .help-text {
          display: block;
          font-size: 14px;
          color: #666;
          margin-top: 4px;
        }

        .error-message {
          display: block;
          font-size: 14px;
          color: #d32f2f;
          margin-top: 4px;
        }
      `}</style>
    </div>
  );
};

// Text Input component
const TextInput = ({
  id,
  label,
  value,
  onChange,
  required = false,
  type = 'text',
  error = '',
  helpText = '',
  autoComplete = '',
  ...props
}) => {
  const helpId = helpText ? `${id}-help` : '';
  const errorId = error ? `${id}-error` : '';
  const describedBy = [helpId, errorId].filter(Boolean).join(' ');

  return (
    <FormField error={error} helpText={helpText}>
      <label htmlFor={id}>
        {label}
        {required && <span className="required" aria-label="required"> *</span>}
      </label>
      <input
        type={type}
        id={id}
        value={value}
        onChange={onChange}
        required={required}
        aria-required={required}
        aria-invalid={!!error}
        aria-describedby={describedBy || undefined}
        autoComplete={autoComplete}
        {...props}
      />
      <style jsx>{`
        label {
          display: block;
          margin-bottom: 5px;
          font-weight: bold;
        }

        .required {
          color: #d32f2f;
        }

        input {
          width: 100%;
          padding: 8px;
          border: 2px solid ${error ? '#d32f2f' : '#ccc'};
          border-radius: 4px;
          font-size: 16px;
        }

        input:focus {
          outline: 2px solid #005eb8;
          outline-offset: 2px;
        }
      `}</style>
    </FormField>
  );
};

// Select Input component
const SelectInput = ({
  id,
  label,
  value,
  onChange,
  options,
  required = false,
  error = '',
  ...props
}) => {
  const errorId = error ? `${id}-error` : '';

  return (
    <FormField error={error}>
      <label htmlFor={id}>
        {label}
        {required && <span className="required" aria-label="required"> *</span>}
      </label>
      <select
        id={id}
        value={value}
        onChange={onChange}
        required={required}
        aria-required={required}
        aria-invalid={!!error}
        aria-describedby={errorId || undefined}
        {...props}
      >
        <option value="">Please select</option>
        {options.map(option => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <style jsx>{`
        label {
          display: block;
          margin-bottom: 5px;
          font-weight: bold;
        }

        .required {
          color: #d32f2f;
        }

        select {
          width: 100%;
          padding: 8px;
          border: 2px solid ${error ? '#d32f2f' : '#ccc'};
          border-radius: 4px;
          font-size: 16px;
        }

        select:focus {
          outline: 2px solid #005eb8;
          outline-offset: 2px;
        }
      `}</style>
    </FormField>
  );
};

// Checkbox Group component
const CheckboxGroup = ({
  legend,
  options,
  selectedValues,
  onChange,
  required = false,
  error = '',
}) => {
  const errorId = error ? 'checkbox-group-error' : '';

  const handleChange = (value) => {
    const newValues = selectedValues.includes(value)
      ? selectedValues.filter(v => v !== value)
      : [...selectedValues, value];
    onChange(newValues);
  };

  return (
    <fieldset>
      <legend>
        {legend}
        {required && <span className="required" aria-label="required"> *</span>}
      </legend>

      {options.map(option => (
        <div key={option.value} className="checkbox-wrapper">
          <input
            type="checkbox"
            id={option.value}
            value={option.value}
            checked={selectedValues.includes(option.value)}
            onChange={() => handleChange(option.value)}
            aria-describedby={errorId || undefined}
          />
          <label htmlFor={option.value}>{option.label}</label>
        </div>
      ))}

      {error && (
        <span id={errorId} className="error-message" role="alert">
          {error}
        </span>
      )}

      <style jsx>{`
        fieldset {
          border: 1px solid #ccc;
          padding: 15px;
          margin-bottom: 20px;
        }

        legend {
          font-weight: bold;
          padding: 0 5px;
        }

        .required {
          color: #d32f2f;
        }

        .checkbox-wrapper {
          margin-bottom: 10px;
        }

        input[type="checkbox"] {
          margin-right: 8px;
        }

        input[type="checkbox"]:focus {
          outline: 2px solid #005eb8;
          outline-offset: 2px;
        }

        .error-message {
          display: block;
          font-size: 14px;
          color: #d32f2f;
          margin-top: 8px;
        }
      `}</style>
    </fieldset>
  );
};

// Radio Group component
const RadioGroup = ({
  legend,
  name,
  options,
  selectedValue,
  onChange,
  required = false,
  error = '',
}) => {
  const errorId = error ? `${name}-error` : '';

  return (
    <fieldset>
      <legend>
        {legend}
        {required && <span className="required" aria-label="required"> *</span>}
      </legend>

      {options.map(option => (
        <div key={option.value} className="radio-wrapper">
          <input
            type="radio"
            id={option.value}
            name={name}
            value={option.value}
            checked={selectedValue === option.value}
            onChange={(e) => onChange(e.target.value)}
            required={required}
            aria-required={required}
            aria-describedby={errorId || undefined}
          />
          <label htmlFor={option.value}>{option.label}</label>
        </div>
      ))}

      {error && (
        <span id={errorId} className="error-message" role="alert">
          {error}
        </span>
      )}

      <style jsx>{`
        fieldset {
          border: 1px solid #ccc;
          padding: 15px;
          margin-bottom: 20px;
        }

        legend {
          font-weight: bold;
          padding: 0 5px;
        }

        .required {
          color: #d32f2f;
        }

        .radio-wrapper {
          margin-bottom: 10px;
        }

        input[type="radio"] {
          margin-right: 8px;
        }

        input[type="radio"]:focus {
          outline: 2px solid #005eb8;
          outline-offset: 2px;
        }

        .error-message {
          display: block;
          font-size: 14px;
          color: #d32f2f;
          margin-top: 8px;
        }
      `}</style>
    </fieldset>
  );
};

// Example usage component
const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    preferences: [],
    contactMethod: '',
  });

  const [errors, setErrors] = useState({});
  const [submitted, setSubmitted] = useState(false);

  const validate = () => {
    const newErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = 'Please enter your name';
    }

    if (!formData.email.trim()) {
      newErrors.email = 'Please enter your email';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    if (!formData.subject) {
      newErrors.subject = 'Please select a subject';
    }

    if (formData.preferences.length === 0) {
      newErrors.preferences = 'Please select at least one preference';
    }

    if (!formData.contactMethod) {
      newErrors.contactMethod = 'Please select a contact method';
    }

    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const newErrors = validate();
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      // Form is valid
      console.log('Form submitted:', formData);
      setSubmitted(true);

      // Reset form after 3 seconds
      setTimeout(() => {
        setFormData({
          name: '',
          email: '',
          subject: '',
          preferences: [],
          contactMethod: '',
        });
        setSubmitted(false);
      }, 3000);
    }
  };

  return (
    <div>
      <h1>Contact Form</h1>

      {submitted && (
        <div className="success-message" role="status" aria-live="polite">
          Thank you! Your form has been submitted successfully.
        </div>
      )}

      <form onSubmit={handleSubmit} noValidate>
        <TextInput
          id="name"
          label="Name"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          required
          error={errors.name}
          helpText="Enter your full name"
          autoComplete="name"
        />

        <TextInput
          id="email"
          label="Email Address"
          type="email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          required
          error={errors.email}
          helpText="We'll use this to contact you"
          autoComplete="email"
        />

        <SelectInput
          id="subject"
          label="Subject"
          value={formData.subject}
          onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
          required
          error={errors.subject}
          options={[
            { value: 'general', label: 'General Enquiry' },
            { value: 'admissions', label: 'Admissions' },
            { value: 'research', label: 'Research' },
            { value: 'support', label: 'Technical Support' },
          ]}
        />

        <CheckboxGroup
          legend="Communication Preferences"
          required
          options={[
            { value: 'email', label: 'Email updates' },
            { value: 'phone', label: 'Phone calls' },
            { value: 'post', label: 'Postal mail' },
          ]}
          selectedValues={formData.preferences}
          onChange={(values) => setFormData({ ...formData, preferences: values })}
          error={errors.preferences}
        />

        <RadioGroup
          legend="Preferred Contact Method"
          name="contact-method"
          required
          options={[
            { value: 'email', label: 'Email' },
            { value: 'phone', label: 'Phone' },
          ]}
          selectedValue={formData.contactMethod}
          onChange={(value) => setFormData({ ...formData, contactMethod: value })}
          error={errors.contactMethod}
        />

        <button type="submit">Submit Form</button>
      </form>

      <style jsx>{`
        .success-message {
          background-color: #d4edda;
          color: #155724;
          padding: 12px;
          border-radius: 4px;
          margin-bottom: 20px;
        }

        button[type="submit"] {
          background-color: #005eb8;
          color: white;
          padding: 12px 24px;
          border: none;
          border-radius: 4px;
          font-size: 16px;
          cursor: pointer;
        }

        button[type="submit"]:hover {
          background-color: #004a94;
        }

        button[type="submit"]:focus {
          outline: 2px solid #005eb8;
          outline-offset: 2px;
        }
      `}</style>
    </div>
  );
};

export {
  FormField,
  TextInput,
  SelectInput,
  CheckboxGroup,
  RadioGroup,
  ContactForm
};
